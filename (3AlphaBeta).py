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



#Enter 8 leaf node values:
#3 5 6 9 1 2 0 -1
#Optimal value for maximizing player: 5



#1. Start the program.
#2. Define the Alpha-Beta Pruning function.
#3. Check if the current node is a leaf node.
#4. If it is a leaf node, return its value.
#5. If the current player is maximizing:
#    * Initialize best value to a very small number.
#    * Recursively evaluate child nodes.
#    * Update the best value and alpha value.
#    * Apply pruning if beta ≤ alpha.
#6. If the current player is minimizing:
#    * Initialize best value to a very large number.
#    * Recursively evaluate child nodes.
#    * Update the best value and beta value.
#    * Apply pruning if beta ≤ alpha.
#7. Input 8 leaf node values from the user.
#8. Call the Alpha-Beta function with initial alpha and beta values.
#9. Display the optimal value for the maximizing player.
#10. End the program.
