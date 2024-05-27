import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.model_selection import GridSearchCV

# Import the dataset
data = pd.read_csv('diabetes_dirty.csv')

# Define independent variables
X_feature = data.drop(['AGE','SEX','S1','S2','PROGRESSION'], axis=1)

# Define dependent variables
y_target = data['PROGRESSION']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_feature, y_target, test_size=0.2, random_state=42)

# Apply StandardScaler
standard_scaler = StandardScaler()
X_train_standard = standard_scaler.fit_transform(X_train)
X_test_standard = standard_scaler.transform(X_test)

# Random Forest Regressor
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train_standard, y_train)
y_pred_rf = rf_model.predict(X_test_standard)

mse_rf = mean_squared_error(y_test, y_pred_rf)
r2_rf = r2_score(y_test, y_pred_rf)

print("Random Forest Regressor - MSE: ", mse_rf)
print("Random Forest Regressor - R2 Score: ", r2_rf)

# Gradient Boosting Regressor
gb_model = GradientBoostingRegressor(n_estimators=100, random_state=42)
gb_model.fit(X_train_standard, y_train)
y_pred_gb = gb_model.predict(X_test_standard)

mse_gb = mean_squared_error(y_test, y_pred_gb)
r2_gb = r2_score(y_test, y_pred_gb)

print("Gradient Boosting Regressor - MSE: ", mse_gb)
print("Gradient Boosting Regressor - R2 Score: ", r2_gb)

# Hyperparameter Tuning for Random Forest
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

grid_search_rf = GridSearchCV(estimator=RandomForestRegressor(random_state=42),
                              param_grid=param_grid,
                              cv=5, n_jobs=-1, verbose=2)

grid_search_rf.fit(X_train_standard, y_train)

best_params_rf = grid_search_rf.best_params_
print("Best parameters for Random Forest: ", best_params_rf)

best_rf_model = grid_search_rf.best_estimator_
y_pred_best_rf = best_rf_model.predict(X_test_standard)

mse_best_rf = mean_squared_error(y_test, y_pred_best_rf)
r2_best_rf = r2_score(y_test, y_pred_best_rf)

print("Best Random Forest Regressor - MSE: ", mse_best_rf)
print("Best Random Forest Regressor - R2 Score: ", r2_best_rf)
