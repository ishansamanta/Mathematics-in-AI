x = [i for i in range(1,7)]
y_true = [2*i for i in range(1,7)]
best_error = float('inf')   
best_w = 0
best_b = 0
for w in range(-10,11):
    for b in range(-10,11):
        total_error = 0   

        for i in range(len(x)):
            y_pred = w * x[i] + b
            total_error += (y_true[i] - y_pred) ** 2
        if total_error < best_error:
            best_error = total_error
            best_w = w
            best_b = b
print("Best w:", best_w)
print("Best b:", best_b)
print("Minimum total error:", best_error)
