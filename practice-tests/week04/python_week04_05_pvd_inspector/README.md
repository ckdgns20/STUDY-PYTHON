# PVD Semiconductor Process Data Inspector

실제 반도체 PVD(Physical Vapor Deposition) 공정 데이터를 활용하여 CSV 데이터를 읽고, 데이터 구조와 기본 상태를 확인하는 Python 미니프로젝트입니다.

이 프로젝트는 Python의 **함수, 모듈, import, return, docstring, `__main__`** 개념을 실제 반도체 제조 데이터에 적용하는 것을 목표로 합니다.

현재 단계에서는 데이터 분석이나 머신러닝보다 **프로그램을 역할별로 분리하고 실제 데이터를 안정적으로 읽고 확인하는 과정**에 집중합니다.

---

## Project Objective

PVD 공정의 APC 입력 데이터와 SPC 막 두께 측정 데이터를 불러와 다음 정보를 확인하는 프로그램을 구현합니다.

* CSV 데이터 정상 로드 여부
* 데이터의 행/열 개수
* 결측값 존재 여부 및 개수
* Thickness 관련 column 탐색
* X/Y sample 수 일치 여부
* 데이터 구조 요약 출력

---

## Dataset

본 프로젝트에서는 공개된 **PVD APC/SPC Dataset**을 사용합니다.

Dataset:

https://zenodo.org/records/16881338


## Project Structure

```text
pvd_inspector/
│
├── main.py
├── data_loader.py
├── data_utils.py
├── utils.py
│
└── README.md
```

## Learning Objectives

이 프로젝트를 통해 다음 Python 개념을 연습합니다.

* 함수 정의와 호출
* Parameter와 Argument
* `return`
* 다중 반환
* Python Module
* `import module`
* `from module import function`
* docstring
* 파일 입출력
* CSV 처리
* 모듈 간 역할 분리
* `if __name__ == "__main__":`
* Import Error 디버깅

---

## Development Rules

현재 단계에서는 다음 라이브러리를 사용하지 않습니다.

```text
pandas
NumPy
scikit-learn
PyTorch
```

Python 기본 문법과 표준 라이브러리인 `csv`를 이용하여 직접 데이터를 처리합니다.

이는 데이터 분석 성능을 높이는 것이 아니라 **Python 데이터 처리 구조를 이해하는 것**이 현재 학습 목표이기 때문입니다.

---

## Progress

### Data Loading

* [ ] X CSV 파일 읽기
* [ ] Y CSV 파일 읽기
* [ ] Header 분리
* [ ] Data rows 분리

### Data Inspection

* [ ] X 행/열 개수 계산
* [ ] Y 행/열 개수 계산
* [ ] 결측값 개수 계산
* [ ] X/Y sample 수 비교

### Python Structure

* [ ] `data_loader.py` 생성
* [ ] `utils.py` 생성
* [ ] `main.py`에서 모듈 import
* [ ] 함수별 docstring 작성
* [ ] `if __name__ == "__main__":` 적용


## Current Scope

현재 프로젝트에서는 다음 작업까지만 진행합니다.

```text
Data Loading
    ↓
Data Structure Inspection
    ↓
Data Validation
    ↓
Summary
```

다음 내용은 아직 구현하지 않습니다.

```text
EDA
Visualization
Correlation Analysis
Feature Selection
Machine Learning
Deep Learning
Virtual Metrology
Anomaly Detection
Root Cause Analysis
Process Optimization
```

---

## Future Development

본 프로젝트는 Python 학습이 진행됨에 따라 동일한 PVD 데이터를 이용해 지속적으로 확장할 예정입니다.

```text
PVD Data Inspector
        ↓
NumPy Data Analysis
        ↓
Pandas EDA
        ↓
Data Visualization
        ↓
17-Point Thickness Analysis
        ↓
Virtual Metrology
        ↓
Spatial Thickness Modeling
        ↓
Anomaly Detection
        ↓
Root Cause Analysis
        ↓
Process Recommendation
        ↓
Advanced Process Control
```

최종 연구 주제나 모델을 처음부터 고정하지 않고, 데이터를 지속적으로 분석하면서 기존 접근과 다른 문제를 발견하는 것을 장기적인 목표로 합니다.

---
