# Pandas 뿌수기

> 참고 사이트 : <https://pandas.pydata.org/docs/user_guide/10min.html#operations>

## 라이브러리 import

```python
import numpy as np
import pandas as pd
```

---

## csv 파일 불러오기

```python
csv_file = pd.read_csv('파일명.csv', sheet_name='스프레드시트명')
```

---

## 받은 csv 파일 데이터프레임으로 변환

```python
df_csv_file = pd.DataFrame(csv_file)
df_csv_file = pd.DataFrame(csv_file[0:10]) # 0~10줄 까지
```

> 데이터프레임으로 변환하면 데이터 조작이 쉬워진다.

---

## 데이터프레임을 넘파이 배열로 변환

```python
df_csv_file.to_numpy()
```

> 넘파이 행렬 연산이 가능하기 때문에 변환하면 좋다

---

## 열 참조 방법

```python
df_csv_file['행 head 이름']
```

> 행 이름을 그대로 작성해준다.
>
> 행 하나만 불러올때 사용

---
