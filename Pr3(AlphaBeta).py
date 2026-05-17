# Alpha Beta Pruning

def alpha_beta(node, depth, alpha, beta, maximizing_player, values):

    # Leaf node condition
    if depth == 3:
        return values[node]

    # Maximizing player
    if maximizing_player:

        best_value = -1000

        for i in range(2):

            value = alpha_beta(node * 2 + i,
                               depth + 1,
                               alpha,
                               beta,
                               False,
                               values)

            best_value = max(best_value, value)

            alpha = max(alpha, best_value)

            # Pruning condition
            if beta <= alpha:
                break

        return best_value

    # Minimizing player
    else:

        best_value = 1000

        for i in range(2):

            value = alpha_beta(node * 2 + i,
                               depth + 1,
                               alpha,
                               beta,
                               True,
                               values)

            best_value = min(best_value, value)

            beta = min(beta, best_value)

            # Pruning condition
            if beta <= alpha:
                break

        return best_value


# Taking input from user
print("Enter 8 leaf node values:")

values = list(map(int, input().split()))

# Calling function
result = alpha_beta(0, 0, -1000, 1000, True, values)

print("Optimal value for maximizing player:", result)