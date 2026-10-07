import numpy as np


class DataAnalyzer:


    def array_management(self):

        while True:

            print('''=================================
Select the type of array to create:
1. 1D Array
2. 2D Array
3. 3D Array
4. Exit
=================================''')

            val = input('Enter your choice: ')

            match val:

                case '1':

                    n = int(input('Enter the number of elements: '))

                    elements = list(map(int, input(f'Enter {n} elements separated by space: ').split()))

                    self.arr = np.array(elements)

                    print(self.arr)
                    print('1D Array Created Successfully...')


                case '2':

                    r1 = int(input('Enter the number of rows: '))
                    r2 = int(input('Enter the number of columns: '))

                    elements = list(map(int, input(f'Enter {r1 * r2} elements separated by space: ').split()))

                    self.arr = np.array(elements).reshape(r1, r2)

                    print(self.arr)
                    print('2D Array Created Successfully...')


                case '3':

                    r1 = int(input('Enter the number of rows: '))
                    r2 = int(input('Enter the number of columns: '))
                    r3 = int(input('Enter the number of layers: '))

                    elements = list(map(int, input(f'Enter {r1 * r2 * r3} elements separated by space: ').split()))

                    self.arr = np.array(elements).reshape(r1, r2, r3)

                    print(self.arr)
                    print('3D Array Created Successfully...')


                case '4':

                    print('Going back...')
                    break


                case _:

                    print('Invalid Choice...')


    # ================= MATHEMATICAL OPERATIONS =================

    def arr_math(self):

        while True:

            print('''=================================
Choose a mathematical operation:
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit
=================================''')

            val = input('Enter your choice: ')

            match val:

                case '1':

                    new = list(map(int, input('Enter the same elements separated by space: ').split()))

                    new_arr = np.array(new).reshape(self.arr.shape)

                    self.arr = self.arr + new_arr

                    print('After adding:')
                    print(self.arr)


                case '2':

                    new = list(map(int, input('Enter the same elements separated by space: ').split()))

                    new_arr = np.array(new).reshape(self.arr.shape)

                    self.arr = self.arr - new_arr

                    print('After subtracting:')
                    print(self.arr)


                case '3':

                    new = list(map(int, input('Enter the same elements separated by space: ').split()))

                    new_arr = np.array(new).reshape(self.arr.shape)

                    self.arr = self.arr * new_arr

                    print('After multiplying:')
                    print(self.arr)


                case '4':

                    new = list(map(int, input('Enter the same elements separated by space: ').split()))

                    new_arr = np.array(new).reshape(self.arr.shape)

                    self.arr = self.arr / new_arr

                    print('After dividing:')
                    print(self.arr)


                case '5':

                    print('Exiting mathematical operations...')
                    break


                case _:

                    print('Invalid choice!!')



    def comb_spl(self):

        while True:

            print('''=================================
Choose an option:
1. Combine Arrays
2. Split Arrays
3. Exit
=================================''')

            val = input('Enter your choice: ')

            match val:

                case '1':
                    elements = list(map(int, input('Enter elements for second array: ').split()))

                    
                    arr2 = np.array(elements).reshape(self.arr.shape)

                    combined = np.concatenate((self.arr, arr2))

                    print('First array:')
                    print(self.arr)

                    print('Second array:')
                    print(arr2)

                    print('Combined array:')
                    print(combined)



                case '2':

                    split_arr = np.array_split(self.arr, 2)
                    

                    print('Array after splitting into 2 parts:')

                    for self.arr in split_arr:
                        print(self.arr)


                case '3':

                    print('Exiting...')
                    break


                case _:

                    print('Invalid choice!!')




    def aggri_static(self):

        while True:

            print('''=================================
Choose an option:
1. Sum
2. Mean
3. Median
4. Standard Deviation
5. Variance
6. Exit
=================================''')

            val = input('Enter your choice: ')

            match val:

                case '1':

                    print(f'Sum: {np.sum(self.arr)}')


                case '2':

                    print(f'Mean: {np.mean(self.arr)}')


                case '3':

                    print(f'Median: {np.median(self.arr)}')


                case '4':

                    print(f'Standard Deviation: {np.std(self.arr)}')


                case '5':

                    print(f'Variance: {np.var(self.arr)}')


                case '6':

                    print('Exiting...')
                    break


                case _:

                    print('Invalid choice!!')
        
    def short_filt(self):
        while True:
                print('''============================
Choose an option : 
1. Search a value 
2. Short a value
3. Filter values
4. Go back...
''')
                val = input('Enter your choice : ')
                match val:
                    
                    case '1':
                        value = int(input('Enter the value to search: '))

                        if value in self.arr:
                            print(f'{value} is present in the array.')
                        else:
                            print(f'{value} is not present in the array.')
                    
                    case '2':
                                
                        sorted_arr = np.sort(self.arr)

                        print('Original array:')
                        print(self.arr)

                        print('Sorted array:')
                        print(sorted_arr)
                        
                    case '3':
                        print('''========================
                        Choose an option :
                        1. Filter by even numbers 
                        2. filter by odd numners
                        3. Exit...
                        ========================''')
                        val = input('Enter your choice : ')
                        match val:
                            case '1':  
                                mask = self.arr % 2 == 0
                                filtered_arr = self.arr[mask]
                                print(filtered_arr)
                                
                            case '2':
                                mask = self.arr % 2 != 0
                                filtered_arr = self.arr[mask]
                                print(filtered_arr)
                                
                            case '3':
                                print('Exit...')
                                break
                    case '4':
                        break
                                               


a = DataAnalyzer()
while True:

    print('''==================================== 
<<-------- WELCOME TO THE NUMPY ANALYZER -------->> 
Choose an option 
1. Create a Numpy Array. 
2. Perform Mathematical Operaion. 
3. Combine or Split Array. 
4. Search, Sort or Filter Array. 
5. Compute Aggregates and Statistics
6. Exit... 
====================================''')

    val = input('Enter Your choice : ')
    match val:
        case '1':
            a.array_management()
        
        case '2':
            a.arr_math()
            
        case '3':
            a.comb_spl()
        
        case '4':
            a.short_filt()
        
        case '5':
            a.aggri_static()
            
        case '6':
            print("Exiting...")
            break
        
        case _:
            print('Invalid Choice!')
            
