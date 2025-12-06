## Bài tập về nhà: làm kéo búa bao. ghi điểm, thắng +1, hòa + 0.5; chênh lêc̣ch 2 điềm là thắng, in ra lịch ử trò chơi


nguoi = input('Người ra: ')
while (nguoi not in ['kéo', 'búa', 'bao']):
    nguoi = input('Người nhập lại: ')

import random as r

may = r.choice(['kéo', 'búa', 'bao'])  # choices : tạo ra nhiều giá trị; choice: chọn  giá trị
print('Máy ra: ', may)
if nguoi == may:
    print('Hoà')
elif (nguoi == 'bao' and may == 'búa') or \
        (nguoi == 'kéo' and may == 'bao') or \
        (nguoi == 'búa' and may == 'kéo'):
    print('Người thắng máy')
else:
    print('Người thua máy')

# if nguoi=='kéo' and may=='búa' :
#     print('Người thua máy')
# elif nguoi=='kéo' and may=='bao' :
#     print('Người thắng máy')
# elif nguoi=='búa' and may=='bao' :
#     print('Người thua máy')
# elif nguoi=='búa' and may=='kéo' :
#     print('Người thắng máy')
# elif nguoi=='bao' and may=='kéo' :
#     print('Người thua máy')
# elif nguoi == 'bao' and may == 'bao':
#     print('Hoà')
# elif nguoi == 'kéo' and may == 'kéo':
#     print('Hoà')
# elif nguoi == 'búa' and may == 'búa':
#     print('Hoà')
# else: #nguoi=='bao' and may=='búa'
#     print('Người thắng máy')
