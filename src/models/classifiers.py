from dataclasses import dataclass
from typing import Any, Dict, List
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score

@dataclass
class ClassifierResult:
    name: str
    model: Any
    cv_mean_score: float
    cv_std_score: float

def get_classifier(name: str) -> Any:
    """Factory function returning sklearn classifiers."""
    classifiers = {
        'random_forest': RandomForestClassifier(),
        'gradient_boosting': GradientBoostingClassifier(),
        'logistic_regression': LogisticRegression(),
        'svm': SVC(probability=True)
    }
    if name not in classifiers:
        raise ValueError(f"Classifier {name} not supported.")
    return classifiers[name]

def compare_classifiers(X: Any, y: Any, classifiers: List[str], cv: int = 5) -> List[ClassifierResult]:
    """Compare multiple classifiers using cross-validation."""
    results = []
    for name in classifiers:
        clf = get_classifier(name)
        scores = cross_val_score(clf, X, y, cv=cv, scoring='accuracy')
        results.append(ClassifierResult(
            name=name,
            model=clf,
            cv_mean_score=scores.mean(),
            cv_std_score=scores.std()
        ))
    return sorted(results, key=lambda x: x.cv_mean_score, reverse=True)
