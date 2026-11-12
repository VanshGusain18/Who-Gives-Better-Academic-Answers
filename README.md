# Who Gives Better Academic Answers?
## ChatGPT/LLMs vs Teachers — Student Perception Study

## 1. Project Overview

This project investigates undergraduate students' perceptions of teacher-given and LLM-generated academic explanations.

The study compares students' perceptions of:
- Accuracy
- Clarity
- Conceptual understanding
- Practical usefulness
- Ease of understanding
- Trustworthiness
- Task-based preferences
- Reasons for preferring teachers or LLMs

The project uses survey responses, statistical analysis, NLP, semantic analysis, and qualitative theme extraction.

The study evaluates student perceptions and does not automatically establish objective superiority of either source.

## 2. Team Structure and File Ownership

Each project member is assigned specific files and folders.

### Member 1 — Data Processing, Cleaning, GitHub and Integration
**Owner: Member 1**

Responsibilities:
- GitHub repository administration
- Dataset schema definition
- Synthetic dataset creation
- Raw data management
- Data inspection and cleaning
- Data validation
- Data preprocessing
- Final pipeline integration
- Final results organization

Owned files and folders:
- `README.md`
- `requirements.txt`
- `.gitignore`
- `data/`
- `src/data_processing.py`
- `notebooks/01_data_processing.ipynb`
- `notebooks/05_final_pipeline.ipynb`
- `results/final/`
- `paper/introduction.md`

### Member 2 — NLP and Text Analysis
**Owner: Member 2**

Responsibilities:
- Text preprocessing for NLP
- Sentiment analysis
- TF-IDF
- Important word extraction
- Text-based visualizations
- NLP output interpretation

Owned files and folders:
- `src/sentiment_tfidf.py`
- `notebooks/02_nlp_analysis.ipynb`
- `results/sentiment/`
- `paper/literature_review.md`

### Member 3 — Semantic Analysis
**Owner: Member 3**

Responsibilities:
- Sentence embeddings
- Semantic similarity
- Clustering
- Theme extraction
- Semantic analysis visualizations
- Theme validation

Owned files and folders:
- `src/semantic_analysis.py`
- `notebooks/03_semantic_analysis.ipynb`
- `results/semantic/`
- `paper/methodology.md`

### Member 4 — Statistical Analysis
**Owner: Member 4**

Responsibilities:
- Descriptive statistics
- Likert-scale analysis
- Paired comparisons
- Statistical hypothesis testing
- Correlation and categorical association
- Statistical visualizations
- Interpretation of statistical findings

Owned files and folders:
- `src/statistical_analysis.py`
- `notebooks/04_statistical_analysis.ipynb`
- `results/statistics/`
- `paper/statistical_methodology.md`

### Shared Ownership
All members contribute to:
- `paper/final_paper.md`
- Final discussion and conclusions
- Research interpretation
- Presentation and viva preparation

## 3. Repository Structure

```text
Who-Gives-Better-Academic-Answers/
│
├── README.md                         [Member 1]
├── requirements.txt                  [Member 1]
├── .gitignore                       [Member 1]
│
├── data/
│   ├── synthetic/                    [Member 1]
│   └── real/                         [Member 1]
│
├── src/
│   ├── data_processing.py            [Member 1]
│   ├── sentiment_tfidf.py            [Member 2]
│   ├── semantic_analysis.py           [Member 3]
│   └── statistical_analysis.py        [Member 4]
│
├── notebooks/
│   ├── 01_data_processing.ipynb      [Member 1]
│   ├── 02_nlp_analysis.ipynb         [Member 2]
│   ├── 03_semantic_analysis.ipynb     [Member 3]
│   ├── 04_statistical_analysis.ipynb  [Member 4]
│   └── 05_final_pipeline.ipynb        [Member 1]
│
├── results/
│   ├── sentiment/                     [Member 2]
│   ├── semantic/                      [Member 3]
│   ├── statistics/                    [Member 4]
│   └── final/                         [Member 1]
│
└── paper/
    ├── introduction.md                [Member 1]
    ├── literature_review.md           [Member 2]
    ├── methodology.md                 [Member 3]
    ├── statistical_methodology.md     [Member 4]
    └── final_paper.md                 [All members]
```

## 4. File Ownership Rules

1. Each member is the primary maintainer of their assigned files.
2. Members must not directly modify another member's owned implementation files without permission.
3. All members may review code and suggest improvements.
4. Shared interfaces and dataset schemas must be agreed upon before changes.
5. Changes to the dataset schema must be communicated to all members.
6. Changes to another member's files should preferably be submitted through a Pull Request.
7. Member 1 coordinates integration into the final pipeline.
8. Ownership indicates responsibility, not an automatic GitHub file lock.

## 5. Development Workflow

The project uses parallel development.

1. Member 1 prepares the repository, dataset schema, and synthetic dataset.
2. All members develop their assigned modules using synthetic data.
3. Members independently test their implementations.
4. Each module is integrated with the common cleaned dataset.
5. Actual survey responses replace synthetic data for final analysis.
6. All modules are executed on actual survey responses.
7. Results are validated and documented.
8. The final research paper is completed.

Synthetic data must never be presented as actual participant responses or used to claim research findings.

## 6. Technology Stack

- Python
- Google Colab
- GitHub
- Pandas
- NumPy
- SciPy
- scikit-learn
- Transformers / Hugging Face
- Sentence Transformers
- Matplotlib
- Seaborn
- Statsmodels

## 7. Data Management

- Raw survey data must remain unchanged.
- Cleaning must produce separate processed datasets.
- Synthetic and real datasets must remain separate.
- Real participant responses must be anonymized.
- Identifiable or confidential survey data must not be committed to a public repository.
- Data cleaning decisions must be documented.
- Final results must be reproducible from the approved dataset and code.

## 8. Collaboration

- GitHub is the primary source of code and project documentation.
- Google Colab is used for cloud-based execution.
- Each member works primarily on their assigned files.
- Members should commit and push changes regularly.
- Pull Requests should be reviewed before integration.
- Integration checkpoints should occur every 2–3 days.
- The final pipeline must run from beginning to end.

## 9. Research Integrity

- Synthetic responses are only for development and testing.
- Actual survey responses are used for research analysis.
- Findings must be based on actual collected data.
- NLP sentiment must not be interpreted as objective explanation quality.
- Statistical conclusions must follow the assumptions and limitations of the selected tests.
- No results or participant responses may be fabricated for the final research paper.
