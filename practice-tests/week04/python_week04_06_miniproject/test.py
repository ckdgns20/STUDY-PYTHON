results = results = {
    'A': {'acc': -0.95, 'ms': 0.50},
    'B': {'acc': 0.97, 'ms': 0.65},
    'C': {'acc': 0.94, 'ms': 0.40}
}

def validate_results(results):
    '''
    추론 시간 ms가 가장 짧은 모델을 찾음
    results: input data(dict)
    return : is_valid, errors
    '''
    is_valid = True
    errors = []
    if type(results) != dict :
        errors.append('results는 딕셔너리여야 합니다.')
        is_valid = False
    elif not results:
        errors.append('results가 비어 있습니다.')
        is_valid = False

    for model_id, result in results.items():
        if not model_id or not model_id.strip():
            errors.append('모델 ID는 비어 있지 않은 문자열이어야 합니다.')
            is_valid = False

        if type(result) != dict:
            errors.append(f'{model_id}의 결과는 딕셔너리여야 합니다.')
            is_valid = False

        if not 'acc' in result.keys() :
            errors.append(f'{model_id}에 acc 항목이 없습니다.')
            is_valid = False

        if not 'ms' in result.keys() :
            errors.append(f'{model_id}에 ms 항목이 없습니다.')
            is_valid = False

        try :
            if not 0.0 <= result['acc'] <= 1.0 :
                errors.append(f'{model_id}.acc는 0.0 이상 1.0 이하의 유한한 숫자여야 합니다.')
                is_valid = False
        except KeyError :
                errors.append(f'{model_id}.acc 항목이 없어서 값의 범위를 검사 못합니다.')

        try:
            if not 0.0 < result['ms']  :
                errors.append(f'{model_id}.ms는 0보다 큰 유한한 숫자여야 합니다.')
                is_valid = False
        except KeyError :
                errors.append(f'{model_id}.ms 항목이 없어서 값의 범위를 검사 못합니다.')
    
    
    return is_valid, errors

def get_best_accuracy(results):
    '''
    데이터 중 최고 정확도인 실험을 찾는 함수
    results: input data(dict)
    return : model_id, accuracy
    '''
    accuracy = 0
    model_id = []
    for model, result in results.items():
        if result['acc'] > accuracy :
            accuracy = result['acc']
            model_id.clear()
            model_id.append(model)
        elif result['acc'] ==  accuracy:
            model_id.append(model)
    model_id.sort    
    return model_id[0], accuracy

def get_fastest_model(results):
    '''
    추론 시간 ms가 가장 짧은 모델을 찾음
    results: input data(dict)
    return : model_id, inference_ms
    '''
    inference_ms = float('inf')
    model_id = []
    for model, result in results.items():
        if result['ms'] < inference_ms :
            inference_ms = result['ms']
            model_id.clear()
            model_id.append(model)
        elif result['ms'] == inference_ms:
            model_id.append(model)
    model_id.sort    
    
    return model_id[0], inference_ms
    
    
is_valid, errors = validate_results(results)

print(is_valid)
print(errors)

model_id, accuracy = get_best_accuracy(results)

print(model_id, accuracy)

model_id, inference_ms = get_fastest_model(results)

print(model_id, inference_ms)

print((results.values['acc']))