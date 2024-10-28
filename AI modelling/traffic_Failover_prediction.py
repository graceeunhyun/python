# Pandas를 사용해 입력 데이터를 정의하는 예시
import pandas as pd
from sklearn.model_selection import train_test_split  # train_test_split는 model_selection에서 가져옵니다
from sklearn.ensemble import RandomForestClassifier  # RandomForestClassifier는 ensemble에서 가져옵니다
from sklearn.metrics import accuracy_score, classification_report
# 하이퍼 파라미터 튜닝을 수행함 GridSearchCV 나 RandomizedSearchCV를 사용할 수 있음
from sklearn.model_selection import GridSearchCV

# 데이터 예시
data = pd.read_csv('C:\\Users\\user\\Desktop\\Data\\Expanded_Transaction_Data.csv')

# Status 값을 0, 1로 변환
data['Status'] = data['Status'].apply(lambda x: 1 if x == 'FAILED' else 0)

# 입력(feature)와 출력(label) 데이터 분리
X = data[['Response_Time', 'CPU_Usage', 'Memory_Usage', 'I/O_Traffic', 'Network_Latency']]
y = data['Status']

# 학습 데이터와 테스트 데이터로 분리
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 모델 정의
model = RandomForestClassifier(n_estimators=100, random_state=42)

# 모델 학습
model.fit(X_train, y_train)

# 테스트 데이터를 사용한 예측
y_pred = model.predict(X_test)

# 모델 정확도 평가
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# 정밀도, 재현율, F1 점수 확인
print(classification_report(y_test, y_pred, zero_division=0))

# RandomForest 하이퍼파라미터 튜닝
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [10, 20, 30]
}

grid_search = GridSearchCV(RandomForestClassifier(random_state=42), param_grid, cv=5)
grid_search.fit(X_train, y_train)

# 최적의 파라미터 출력
print(grid_search.best_params_)