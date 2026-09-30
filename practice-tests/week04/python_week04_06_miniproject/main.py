from utils import get_fastest_model, get_best_accuracy, get_average_accuracy, validate_results

results = {
    'A': {'acc': 0.95, 'ms': 0.50},
    'B': {'acc': 0.97, 'ms': 0.65},
    'C': {'acc': 0.94, 'ms': 0.40}
}
print(results)
is_valid, errors = validate_results(results)

if not is_valid :
    for error in errors:
        print(error)
else :
    best_name, best_acc = get_best_accuracy(results)
    fast_name, fast_ms = get_fastest_model(results)
    average_acc = get_average_accuracy(results)

    print(f"최고 정확도: {best_name} ({best_acc:.2%})")
    print(f"최고 속도: {fast_name} ({fast_ms:.2f} ms)")
    print(f"평균 정확도: {average_acc:.2%}")
    
print(results)