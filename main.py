input_string = input().strip()
num_queries = int(input().strip())
search_results = []

for _ in range(num_queries):
    query_elements = input().split()
    if query_elements[0] == '0':
        index_to_replace = int(query_elements[1]) - 1
        replacement_char = query_elements[2]
        input_string = input_string[:index_to_replace] + replacement_char + input_string[index_to_replace+1:]
    else:
        substring_to_find = query_elements[1]
        found_index = input_string.find(substring_to_find)
        search_results.append(found_index + 1 if found_index != -1 else found_index)

for result in search_results:
    print(result)
    