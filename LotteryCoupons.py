# There is a  lottery with n coupons and n people take part in it. Each person picks exactly one coupon. Coupons are numbered consecutively from 1 to n. A lottery winner is any person who owns a coupon where the sum of the digits on the coupon is equal to s. if there are multiple winners, the prize is split equally among them. Determine how many values of s there are where there is at least one winner and the prize is split among largest group of people.
# write a function that takes in an integer s and an integer n, and returns the number of values of s where there is at least one winner and the prize is split among largest group of people.
 
def countWinningValues(n):
    max_winners = 0
    count_max_winners = 0

    for s in range(1, 82):  # As the maximum value for s is 81 (9 + 9 + 9 + 9 + 9)
        current_winners = 0

        for i in range(1, n + 1):
            current_winners += sum(int(digit) for digit in str(i)) == s

        if current_winners > max_winners:
            max_winners = current_winners
            count_max_winners = 1
        elif current_winners == max_winners:
            count_max_winners += 1

    return count_max_winners

# Example usage with n = 10
n = 10
result = countWinningValues(n)
print("Number of values of s with the largest group of winners:", result)
