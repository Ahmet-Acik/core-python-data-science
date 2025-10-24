# Core Python Data Science

A comprehensive, modern Python resource for data science, analytics, and automation. This repository is organized for progressive learning and practical reference, from Python basics to advanced OOP and real-world data science workflows.

## Structure

- **basics/**
  - `core_basics.py`: Step-by-step Python fundamentals for data science and scripting.
- **advanced/**
  - `advanced_basics.py`: Advanced Python topics, best practices, and robust scripting.
  - `string_challenge1.py`, `string_challenge2.py`, `string_challenge3.py`: Progressive string coding challenges from interview basics to advanced real-world tasks, with robust unit tests.
- **oop/**
  - `oop_practice.py`: Core OOP concepts and real-world examples.
  - `oop_patterns.py`: Design patterns, SOLID, mixins, composition, protocols, serialization, metaclasses, and OOP in data science.
- **data_science/**
  - `data_loading.py`: Loading data from CSV, Excel, JSON, SQL, APIs.
  - `data_cleaning.py`: Data cleaning, missing values, outliers, string processing.
  - `data_visualization.py`: Visualization with matplotlib, seaborn, pandas, plotly.
  - `numpy_intro.py`: NumPy arrays, math, indexing, broadcasting.
  - `pandas_intro.py`: pandas Series/DataFrame, selection, aggregation, plotting.
  - `matplotlib_intro.py`: Matplotlib plotting basics.
  - `seaborn_intro.py`: Seaborn for statistical and categorical plots.
  - `sklearn_intro.py`: scikit-learn datasets, preprocessing, modeling, pipelines.
  - **datasets/**: Sample datasets (`iris.csv`, `titanic.csv`, `housing.csv`, `mnist_sample.csv`, `weather.csv`, `sales.json`) and code templates for hands-on practice (`*_exercise.py`).

## Latest Developments

- **Datasets folder added:** Includes classic and practical datasets for classification, regression, time series, and JSON analysis, with matching code templates and exercises for each.
- **Advanced string challenges:** Three progressive files covering interview basics, practical string tasks, and advanced real-world string management, all with robust unit tests.
- **Expanded testing coverage:** All major modules and challenge files now have dedicated unit tests for reliability and learning.
- **Practice templates:** Each dataset comes with a matching exercise file for loading, cleaning, EDA, feature engineering, and modeling.



## How to Use

- Each `.py` file is self-contained and runnable for hands-on practice.
- Use the scripts and exercises as templates for your own projects, interview prep, or data science workflows.
- Explore each folder progressively, or jump to the topic or dataset you need.

## Recommended Learning Path

1. Start with `basics/core_basics.py` for Python fundamentals.
2. Move to `advanced/advanced_basics.py` and `advanced/string_challenge1.py` for deeper language features and string mastery.
3. Master OOP in `oop/` with both practice and advanced patterns.
4. Practice data science workflows in `data_science/`, including hands-on exercises with real datasets in `data_science/datasets/`.

## Requirements

- Python 3.10+
- See each file for specific package requirements (e.g., pandas, numpy, matplotlib, seaborn, scikit-learn, plotly).
- Install all requirements with:

  ```sh
  pip install -r requirements.txt
  ```

## Comprehensive Testing

This repository features robust, automated unit tests for all major modules, exercises, and challenge files. The test suite covers:

- **Data science exercises:** All dataset workflows (loading, cleaning, modeling) are tested for correctness and reliability.
- **String challenges:** Progressive string tasks are validated with dedicated unit tests.
- **Core and advanced Python:** Fundamental and advanced features are covered, including OOP, design patterns, and practical utilities.
- **Hands-on templates:** Each code template and exercise is paired with matching tests for learning and validation.

### How to Run All Tests

Activate your Python environment and run all tests with:

```sh
source .venv/bin/activate
python -m unittest discover tests
```

Or, to run all tests in the project (including subfolders):

```sh
python -m unittest discover
```

All tests should pass with no errors or skips. The suite currently includes over 200 tests for comprehensive coverage.

### Best Practices

- All test files follow the `test_*.py` naming convention and use `unittest.TestCase` classes.
- Tests are designed for clarity, reliability, and educational value.
- Add new tests for any new modules, datasets, or exercises to maintain coverage.

## Contributing

Contributions, suggestions, and improvements are welcome! Open an issue or submit a pull request.

---

---

Happy learning and coding!
