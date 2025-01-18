import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
import joblib

# Load dataset
data = pd.read_csv(r"C:\Users\surya kumari\Downloads\StressLevelDataset.csv")

# Specify columns for features
columns_to_consider = [
    'anxiety_level', 'self_esteem', 'mental_health_history', 'depression',
    'headache', 'blood_pressure', 'sleep_quality', 'academic_performance',
    'future_career_concerns', 'bullying'
]

X = data[columns_to_consider]
y = data['stress_level']

# Split into training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train SVM model
model = SVC(kernel='linear')
model.fit(X_train, y_train)

# Save model and scaler
joblib.dump(model, 'svm_model.pkl')
joblib.dump(scaler, 'scaler.pkl')