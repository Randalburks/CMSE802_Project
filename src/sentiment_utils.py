from sklearn.linear_model import LogisticRegression
from sklearn.utils import resample
from sklearn.metrics import accuracy_score, classification_report

def preprocess_reviews(df):
    df = df.dropna(subset=["Review Text"])
    df["Sentiment"] = df["Rating"].apply(lambda x: "Positive" if x >= 4 else ("Neutral" if x == 3 else "Negative"))
    return df

def balance_classes(train_df):
    pos = train_df[train_df.label == "Positive"]
    neu = train_df[train_df.label == "Neutral"]
    neg = train_df[train_df.label == "Negative"]
    neu_upsampled = resample(neu, replace=True, n_samples=len(pos), random_state=42)
    neg_upsampled = resample(neg, replace=True, n_samples=len(pos), random_state=42)
    return pd.concat([pos, neu_upsampled, neg_upsampled])

def train_logistic_regression(X_train, y_train):
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print(classification_report(y_test, y_pred))
