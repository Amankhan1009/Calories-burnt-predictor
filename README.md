# 🏋️ Calories Burnt Prediction using Machine Learning

This project uses machine learning to predict the number of calories burnt during exercise based on various physiological and workout parameters. It includes data preprocessing, model training, hyperparameter tuning, and a deployed Streamlit web app.

---

## 📊 Dataset

The dataset contains features like:

- Gender
- Age
- Height
- Weight
- Duration of exercise
- Heart rate
- Body temperature

It also includes engineered features like:
- **BMI**
- **Effort** (Heart Rate × Duration)

---

## 🚀 Tech Stack

- **Python**
- **Pandas, NumPy, Scikit-learn, XGBoost**
- **Streamlit** (for web app)
- **Matplotlib & Seaborn** (for visualizations)
- **Pickle** (for model serialization)

---

## 🧠 Models Used

| Model                 | Tuned | Notes |
|----------------------|-------|-------|
| Linear Regression     | ❌    | Baseline model |
| Random Forest         | ✅    | Tuned using `RandomizedSearchCV` |
| XGBoost Regressor     | ✅    | Best performance |

---

## 🎯 Final Performance (Sample)

| Model             | MAE   | RMSE  | R² Score |
|------------------|-------|-------|----------|
| Linear Regression| 5.83  | 7.90  | 0.98     |
| Random Forest     | 1.66  | 2.62  | 1.00     |
| **XGBoost**       | **0.96**  | **1.37**  | **1.00** |

---

## Here is the link for you to try it -->
https://amankhan-calories-burnt-predictor.streamlit.app/

------

## 📦 How to Run the App

### 1. Clone the repository

```bash
git clone https://github.com/Amankhan1009/Calories-burnt-predictor
cd calories-burnt-predictor

2. `Install dependencies`
pip install -r requirements.txt

3. ` Run the app locally`


📁 Files in the Repo
`calories.csv` – Input dataset

`calories_model.pkl` – Trained model

`features.pkl` – Feature list used by the model

`calories_app.py` – Streamlit frontend

`notebook.ipynb` – Full data exploration and model training

`README.md` – You’re here!

`requirements.txt` – Python dependencies and all the other Libraries

🙌 Author
Built with 💚 by [Md Aman Alam]
🔗 https://www.linkedin.com/in/md-aman-alam-a04552289/ 

👩‍💻 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
