{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "ba9bc2bf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter a number7\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "8"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def fib(n):\n",
    "        if n==1:\n",
    "            return 0\n",
    "        elif n==2:\n",
    "            return 1\n",
    "        else:\n",
    "            return fib(n-1)+fib(n-2)\n",
    "a=int(input(\"enter a number\"))\n",
    "fib(a)\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "6d276941",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[2, 4]"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "intList=[2,4,5]\n",
    "evenInts=filter(lambda x:x %2==0,intList)\n",
    "list(evenInts)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "30977848",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "745a9d0f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "employees details\n",
      "name:aishu\n",
      "total_salary:21000is total salary of all\n",
      "7000.0is average salary of all\n",
      "name:kipi\n",
      "total_salary:21000is total salary of all\n",
      "7000.0is average salary of all\n",
      "name:nachi\n",
      "total_salary:21000is total salary of all\n",
      "7000.0is average salary of all\n"
     ]
    }
   ],
   "source": [
    "employees=[\n",
    "    {\"name\":\"aishu\",\"salary\":5000},\n",
    "    {\"name\":\"kipi\",\"salary\":7000},\n",
    "    {\"name\":\"nachi\",\"salary\":9000},\n",
    "]\n",
    "total_salary=sum(emp[\"salary\"] for emp in employees)\n",
    "average_salary=total_salary/len(employees)\n",
    "print(\"employees details\")\n",
    "for emp in employees:\n",
    "    print(f\"name:{emp['name']}\")\n",
    "    print(f\"total_salary:{total_salary}is total salary of all\")\n",
    "    print(f\"{average_salary}is average salary of all\")\n",
    "    \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "de1c99b4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "matrix sum:\n",
      " [[ 6  8]\n",
      " [10 12]]\n",
      "matrix product:\n",
      " [[19 22]\n",
      " [43 50]]\n",
      "solution to Ax=B: [2. 3.]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "from scipy import linalg\n",
    "#define to matrices\n",
    "matrix1 = np.array([[1,2],[3,4]])\n",
    "matrix2 = np.array([[5,6],[7,8]])\n",
    "#matrix operations\n",
    "matrix_sum = matrix1 + matrix2\n",
    "matrix_product = np.dot(matrix1,matrix2)\n",
    "print(\"matrix sum:\\n\",matrix_sum)\n",
    "print(\"matrix product:\\n\",matrix_product)\n",
    "#solve a system of linera equtions: Ax = B\n",
    "A = np.array([[3,1],[1,2]])\n",
    "B = np.array([9,8])\n",
    "solution = linalg.solve(A,B)\n",
    "print(\"solution to Ax=B:\",solution)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c360c864",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
