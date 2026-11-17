from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from IPython.display import display

raw_path = Path("/Users/sublee/kbeauty-skin-advisor/data/raw")

df = pd.read_csv(raw_path / "product_info.csv")


print("행(Row) 개수:", df.shape[0])
print("열(Column) 개수:", df.shape[1])
print("전체 데이터 크기:", df.shape)

print("컬럼 목록")
print(df.columns.tolist())

print("\n상위 5개 데이터")
display(df.head())

print("\n하위 5개 데이터")
display(df.tail())


print(f"\n ==== missing values ====")

missing_count = df.isnull().sum()
missing_ratio = df.isnull().mean() * 100

print(f"\n컬럼별 결측치 확인")
print(missing_count.sort_values(ascending=False))
print(f"\n컬럼별 결측치 비율")
print(missing_ratio.sort_values(ascending=False))


print(f"\n==== 중복 데이터 확인 ====")

duplicate_df = df[df.duplicated(keep=False)]

display(duplicate_df.head())


print(f"\n==== 고유값 확인 ====")
unique_count = df.nunique(dropna=False)

unique_df = pd.DataFrame(
    {"unique_count": unique_count, "unique_ratio": unique_count / len(df) * 100}
)

display(unique_df.sort_values(by="unique_count", ascending=False))


print(f"\n==== 수치형, 범주형 데이터 분석 ====")

numeric_df = df.select_dtypes(include=["int64", "float64"])

display(numeric_df.describe().T)


categorical_df = df.select_dtypes(include=["object", "category"])

for col in categorical_df.columns:
    print(f"\n===== {col} =====")

    print("고유값 개수:", df[col].nunique())

    print("\n상위 10개 값")
    display(df[col].value_counts(dropna=False).head(10))


# 가격 분포
if "price_usd" in df.columns:
    plt.figure(figsize=(10, 5))

    sns.histplot(data=df, x="price_usd", bins=50, kde=True)

    plt.title("Product Price Distribution")
    plt.xlabel("Price (USD)")
    plt.ylabel("Count")

    plt.show()

# 카테고리별 평점
if {"primary_category", "rating"}.issubset(df.columns):
    plt.figure(figsize=(12, 7))

    sns.boxplot(data=df, x="primary_category", y="rating")

    plt.xticks(rotation=45)

    plt.title("Rating Distribution by Category")

    plt.tight_layout()
    plt.show()
