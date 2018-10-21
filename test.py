variable = 'value' # assing `value` to variable
print(id(variable)) # print the id i.e. the memory addresses of the variable

x = 10; y = 4
# swap using tuples
x, y = y, x

def vowel_counter(s):
    n = 0
    for i in s:
        if i.lower() in 'aeiou':
            n += 1
    return n

print(vowel_counter("education"))