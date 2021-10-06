import datetime


def Solution(D):
    newD = {'Mon': 0, 'Tue': 0, 'Wed': 0, 'Thu': 0, 'Fri': 0, 'Sat': 0, 'Sun': 0}
    l1 = list(D.keys())
    l2 = list(D.values())

    format = "%Y-%m-%d"

    for i in range(len(l1)):
        l1[i] = datetime.datetime.strptime(l1[i], format)
        l1[i] = l1[i].strftime("%a")
        x = newD.get(l1[i]) + l2[i]
        newD.update({l1[i]: x})

    for i in newD:
        if (i not in l1):
            newD[i] = None

    numbers = list(newD.values())

    def get_right_number(numbers, i):
        if i >= len(numbers) - 1:
            right = None
        else:
            right = numbers[i + 1]
            if right == None:
                right = get_right_number(numbers, i + 1)
        return right

    def clean_missing_data(numbers):

        clean_numbers = []

        for i in range(len(numbers)):
            if numbers[i] != None:
                clean_numbers.append(numbers[i])
            else:
                valid_count = 0

                if i == 0:
                    left = 0
                else:
                    left = clean_numbers[i - 1]
                    valid_count += 1

                right = get_right_number(numbers, i)
                if right == None:
                    right = 0
                else:
                    valid_count += 1

                average = (left + right) / valid_count
                clean_numbers.append(average)
        return clean_numbers

    t = clean_missing_data(numbers)

    y = 0
    for i in newD:
        newD[i] = t[y]
        y += 1

    print(newD)


def main():
    '''test case 1 : normal condition as per question'''
    Solution({'2020-01-01': 4, '2020-01-02': 4, '2020-01-03': 6, '2020-01-04': 5, '2020-01-05': 2, '2020-01-06': -6,
              '2020-01-07': 2, '2020-01-08': -2})

    '''test case 2 : days are missing from the dictionary'''
    Solution({'2020-01-01': 6, '2020-01-04': 12, '2020-01-05': 14, '2020-01-06': 2, '2020-01-07': 4})


if __name__ == '__main__':
    main()
