#############BT1:
#data = '''
#Come to the
#River
#Of my
#Soulful
#Sentiments
#Meandering silently
#Yearning for release.
#Hasten
#Earnestly
#As my love flows by
#Rushing through the flood-gates
#To your heart.

# https://www.poetrysoup.com/poem/cross_my_heart_609765
#Yêu cầu: giải mã mật thư, lấy tất cả các chữ cái đầu của từng dòng rồi ghép lại để được 1 câu cụ thể.

#=>Answer:
a = ['Come to the', 'River', 'Of my', 'Soulful', 'Sentiments', 'Meandering silently', 'Yearning for release', 'Hasten', 'Earnestly', 'As my love flows by', 'Rushing through the flood-gates', 'To your heart']

word = ''

for i in range(len(a)):
        char = a[i][0]
        word = word + char
		
		
print(word)



##################BT2:
#Sử dụng vòng lặp in ra các số từ 1 đến 100, nếu số đó chia hết cho 3 thì thay bằng Buzz, chia hết cho 5 thì thay bằng Fizz, nếu chia hết cho cả 3 và 5 thì thay bằng FizzBuzz. Đồng thời, lưu giữ kết quả đạt được vào 1 list

#=> Answer:

value = []

for i in range(1, 101):
        if i % 3 == 0:
            value.append('Buzz')
        if i % 5 == 0:
            value.append('Fizz')
        if i % 15 == 0:
            value.append('FizzBuzz')

print(value)


#################BT3:
#Viết chương trình loại bỏ phần mở rộng của 1 tên file bất kì VD: newfile.txt -> newfile, photoshop.psd -> photoshop, word.docx -> word, ....


#=> Answer:

file_name = ['newfile.txt', 'photoshop.psd', 'word.docx']


result = []

for name in file_name:
        for char in name:
            if char == '.':
                result.append(name[:name.index(char)])
				
print(result)


#################BT4:

#Có bao nhiêu bộ ba A, B, C thỏa mãn điều kiện sau:

#A, B, C đều là số nguyên dương
#A + B / C = 10
#Lưu các giá trị tìm đc vào 1 list lớn chứa các list con: vd: [[9, 1, 1], ....]


#=> Answer:

result = []

for a in range(1, 20):
        for b in range(1, 20):
            for c in range(1, 20):
                if a * c + b == 10 * c:
                    result.append([a, b, c])

print(result)


###################BT5:

#Luyện tập dùng list comprehension với các câu hỏi sau:
###Tạo 1 list chứa N số 2

list1 = [2 for _ in range(10)]

print(list1)

###Tạo 1 list chứa các số nguyên dương dưới 100, chia hết cho 3 hoặc 5

list2 = [i for i in range(1, 100) if i % 3 == 0 or i % 5 == 0]

print(list2)

###Tạo ra 1 list có dạng như sau: ['111111', '333333', ..., '999999', '111111111111',..., NNNNNN], với N = 20

list3 = [str(i) * 6 for i in range(1, 21) if i % 2 != 0]

print(list3)

###Tạo 1 list chứa N số nguyên ngẫu nhiên, gợi ý sử dụng thư viện random: import random

list4 = []

for i in range(20):
        list4.append(random.randint(0,20))
		
print(list4)


#############################BT6:
#Tính tổng tất cả các số trong kết quả của phép tính 2**10000

#=> Answer:

number = 2 ** 1000
number_ = str(number)
sum_ = 0

for num in number_:
        sum_ = sum_ + int(num)
		
print(sum_)


########################BT7:

#Viết chương trình tính tổng và tích tất cả các số trong 1 list: dùng vòng lặp, ko dùng hàm có sẵn (sum)

### Tính tổng:

number = list(range(20))

sum_ = 0

for i in a:
        sum = sum + int(i)

print(sum_)

### Tính tích:

number = list(range(1, 20))

product = 1

for num in number:
        product = product * int(num)
		
print(product)


#############################BT8:
#iết chương trình tìm số lớn nhất và nhỏ nhất trong 1 list chứa cả kiểu int và float, ko dùng hàm có sẵn (max, min)
### Tìm số nhỏ nhất:

list1 = [1, 2, 3, 4, 5, 6.0, 7.2, 8, 9.5]

for iter in range(1, len(list1)):
        min_num = list1[0]
        if min_num > list1[i]:
            min_num = list[i]
			
print(min_num)

### Tìm số lớn nhất:

list1 = [1, 2, 3, 4, 5, 6.0, 7.2, 8, 9.5]

for iter in range(1, len(list1)):
        max_num = list1[0]
        if max_num > list1[i]:
            max_num = list[i]
			
print(max_num)


###########################BT9:

#Viết chương trình để flatten list sau: [[1, 2, 3], [4, 5], [6, [7, 8], 9], [10]]
#Kết quả cần đạt được: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#=> Answer:

sample = [[1, 2, 3], [4, 5], [6, [7, 8], 9], [10]]

result = []

while sample:
        a = sample.pop()
        if isinstance(a, list) == True:
            sample = sample + a
        else:
            result.append(a)
			
print(result[::-1])


#############################BT10:

import string

alphabets = string.ascii_lowercase

words = ['python', 'patience', 'documents', 'students', 'homework', 'practice', 'success', 'english', 'university', 'congratulation']

result = []

for word in words:
        sum_value = 0
        for char in word:
            sum_value = sum_value + alphabets.index(char) + 1
        result.append([word, sum_value])
		
print(result)




##################################### End of homework of lecture 3 ###########################

