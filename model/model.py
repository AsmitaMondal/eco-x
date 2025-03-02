import pandas as pd
import numpy as np
import joblib
import logging
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor  # type: ignore
from sklearn.metrics import mean_squared_error

# I used logging for my ease of understanding
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

logging.info("Loading dataset...")
df = pd.read_csv("Carbon Emission.csv")

# Some PREPROCESSING
categorical_cols = [
    "Body Type", "Sex", "Diet", "How Often Shower", "Heating Energy Source",
    "Transport", "Vehicle Type", "Social Activity", "Frequency of Traveling by Air",
    "Waste Bag Size", "Energy efficiency", "Recycling", "Cooking_With"
]

numerical_cols = [
    "Monthly Grocery Bill", "Vehicle Monthly Distance Km", "Waste Bag Weekly Count",
    "How Long TV PC Daily Hour", "How Many New Clothes Monthly", "How Long Internet Daily Hour"
]

target_col = "CarbonEmission"

logging.info("Handling missing values...")
for col in df.columns:
    if col in categorical_cols:
        df[col] = df[col].fillna("None") 
    elif col in numerical_cols:
        df[col] = df[col].fillna(df[col].median())  

logging.info("Checking for duplicate rows...")
duplicate_rows = df.duplicated().sum()
logging.info(f"Duplicate rows: {duplicate_rows}")
df.drop_duplicates(inplace=True)

logging.info("Dataset Info:")
logging.info(df.info())

logging.info("Encoding categorical features...")
encoders = {col: LabelEncoder().fit(df[col]) for col in categorical_cols}
for col in categorical_cols:
    df[col] = encoders[col].transform(df[col])

logging.info("Standardizing numerical values...")
scaler = StandardScaler()
df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

# MODEL BUILDING - TRIED TWO BEST ONES TO SEE WHICH ONE PERFORMS BETTER
logging.info("Splitting dataset into train and test sets...")
X = df.drop(columns=[target_col])  
y = df[target_col]  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Hyperparameter tuning for RandomForest
rf_params = {
    'n_estimators': [100, 200],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5],
    'min_samples_leaf': [1, 2]
}
logging.info("Tuning Random Forest hyperparameters...")
rf_params = {
    'n_estimators': [50, 100],  
    'max_depth': [10, 20],      
    'min_samples_split': [2, 5],
    'min_samples_leaf': [1, 2]
}

rf_grid = GridSearchCV(
    RandomForestRegressor(random_state=42), 
    rf_params, 
    cv=2,  
    scoring='neg_mean_squared_error',
    n_jobs=-1,  
    verbose=2   
)
rf_grid.fit(X_train, y_train)
best_rf_model = rf_grid.best_estimator_
rf_pred = best_rf_model.predict(X_test)
rf_rmse = np.sqrt(mean_squared_error(y_test, rf_pred))
logging.info(f"Random Forest Best RMSE: {rf_rmse:.2f}")

# Hyperparameter tuning for XGBoost
xg_params = {
    'n_estimators': [100, 200],
    'learning_rate': [0.05, 0.1],
    'max_depth': [3, 6],
    'subsample': [0.8, 1.0]
}
logging.info("Tuning XGBoost hyperparameters...")
xg_grid = GridSearchCV(XGBRegressor(random_state=42), xg_params, cv=3, scoring='neg_mean_squared_error')
xg_grid.fit(X_train, y_train)
best_xg_model = xg_grid.best_estimator_
xg_pred = best_xg_model.predict(X_test)
xg_rmse = np.sqrt(mean_squared_error(y_test, xg_pred))
logging.info(f"XGBoost Best RMSE: {xg_rmse:.2f}")

# I Saved the best model for my app
if xg_rmse < rf_rmse:
    logging.info("XGBoost performed better. Saving XGBoost model.")
    joblib.dump(best_xg_model, "carbon_model.pkl")
else:
    logging.info("Random Forest performed better. Saving Random Forest model.")
    joblib.dump(best_rf_model, "carbon_model.pkl")

# I also Saved encoders and scaler
logging.info("Saving encoders and scaler...")
joblib.dump(encoders, "encoders.pkl")
joblib.dump(scaler, "scaler.pkl")

logging.info("Training and saving process completed successfully!")
