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