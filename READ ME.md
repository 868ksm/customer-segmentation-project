# README — Проект сегментации клиентов

## Тип проекта

Unsupervised Learning

---

## Описание

Этот проект использует KMeans Clustering для разделения клиентов на группы.

Модель анализирует:

* возраст
* годовой доход
* spending score

AI автоматически создает группы клиентов со схожим поведением.

---

## Technologies Used

* Python
* Flask
* Pandas
* Scikit-learn
* KMeans Clustering
* HTML/CSS

---

## Libraries Used

```python
pandas
scikit-learn
flask
joblib
StandardScaler
```

---

## Project Structure

```bash
customer-segmentation-project/
│
├── app.py
├── train_model.py
├── test_model.py
├── customer_segmentation.csv
├── requirements.txt
├── templates/
├── static/
```

---

## How to Run

### 1. Create virtual environment

```bash
python3 -m venv .venv
```

### 2. Activate environment

```bash
source .venv/bin/activate
```

### 3. Install libraries

```bash
pip install -r requirements.txt
```

### 4. Train model

```bash
python3 train_model.py
```

### 5. Run Flask app

```bash
python3 app.py
```

### 6. Open browser

```text
http://127.0.0.1:5000
```

---

## Алгоритм Machine Learning

KMeans Clustering

---

## Что делает модель

AI группирует клиентов с похожим поведением.

Пример:

```text
высокий доход + большие траты → VIP клиенты
```

---

## Автор

Казыбеков Санжар
Группа: cs24-25
