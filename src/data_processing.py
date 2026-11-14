
import pandas as pd
import re
import html


def clean_text(value):
    if pd.isna(value):
        return pd.NA

    value = html.unescape(str(value))
    value = re.sub(r"\s+", " ", value).strip()

    return value if value else pd.NA


def clean_likert(value):
    if pd.isna(value):
        return pd.NA

    match = re.match(r"^\s*([1-7])(?:\s*(?:=|$))", str(value))

    if match:
        return int(match.group(1))

    return pd.NA


def preprocess_data(input_path, output_path):

    df = pd.read_csv(input_path, encoding="utf-8-sig")

    # Clean column names
    df.columns = df.columns.str.strip()

    # Clean text fields
    for column in df.select_dtypes(include="object").columns:
        df[column] = df[column].apply(clean_text)

    # Normalize consent and age responses
    consent_column = df.columns[1]
    age_column = df.columns[2]

    df[consent_column] = df[consent_column].apply(
        lambda x: "Yes" if str(x).strip().lower() in
        ["i agree", "agree", "yes"] else
        "No" if str(x).strip().lower() in
        ["i do not agree", "do not agree", "no"] else x
    )

    df[age_column] = df[age_column].apply(
        lambda x: "Yes" if str(x).strip().lower() in
        ["yes", "i am 18 years of age or older"] else
        "No" if str(x).strip().lower() in
        ["no", "i am under 18 years of age"] else x
    )

    # Normalize Likert scale columns (Q7–Q15)
    likert_columns = df.columns[7:16]

    # Normalize ChatGPT and Teacher ratings (Q25–Q26)
    rating_columns = df.columns[25:37]

    for column in list(likert_columns) + list(rating_columns):
        df[column] = df[column].apply(clean_likert).astype("Int64")

    # Convert timestamp
    df[df.columns[0]] = pd.to_datetime(
        df[df.columns[0]], errors="coerce", dayfirst=True
    )

    # Save processed dataset
    df.to_csv(output_path, index=False)

    # Summary
    print("Data preprocessing completed successfully!")
    print("-" * 40)
    print("Rows:", len(df))
    print("Columns:", len(df.columns))
    print("Missing values:", df.isna().sum().sum())
    print("Duplicate rows:", df.duplicated().sum())
    print("Output:", output_path)

    return df
