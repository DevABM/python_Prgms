def decode(message_file):
    # Read the lines from the file
    with open(message_file, 'r') as file:
        lines = file.readlines()

    # Initialize a dictionary to store words corresponding to each number
    decoded_words = {}

    # Loop through the lines to decode the message
    for line in lines:
        # Split the line into number and word
        number, word = line.strip().split(' ')
        number = int(number)
        # Store the word corresponding to the number
        decoded_words[number] = word

    # Initialize an empty list to store the decoded message
    decoded_message = []

    # Iterate through the numbers in ascending order to construct the decoded message
    for i in range(1, len(decoded_words) + 1):
        decoded_message.append(decoded_words[i])

    # Join the decoded words to form the final message
    return ' '.join(decoded_message)

# Test the function with an example file
print(decode('coding_qual_input.txt'))
