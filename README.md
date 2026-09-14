# Second Largest

מציאת הערך השני בגודלו ברשימת מספרים, תוך התעלמות מכפילויות.

## דרישות
- Python 3.10+
- pytest

## התקנה
```
git clone https://github.com/oshri-magnezi/second-largest.git
cd second-largest
pip install pytest
```

## שימוש
```python
from main import second_largest

second_largest([3, 7, 2, 9, 5])   # 7
second_largest([4, 4, 4, 2])      # 2
```

הפונקציה זורקת `ValueError` אם אין ברשימה לפחות שני ערכים שונים.

## הרצת הבדיקות
```
pytest -q
```

## מבנה הפרויקט
- `main.py` — הפונקציה `second_largest` והמחלקה `Rectangle`
- `test_second_largest.py` — בדיקות יחידה

## מחבר
אושרי מגנזי