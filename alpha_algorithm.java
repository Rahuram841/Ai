import java.util.Arrays;
import java.util.Scanner;
import java.io.*;
class Matrix_multiplication{
    static void printMatrix(int M[][],
                            int rowSize,
                            int colSize)
    {
        for (int i = 0; i < rowSize; i++) {
            for (int j = 0; j < colSize; j++)
                System.out.print(M[i][j] + " ");
 
            System.out.println();
        }
    }
    public static int[][] multiply(int[][] A,int[][] B)
    {
        int row_1=A[0].length;
        int column_1=A.length;
        System.out.print("row_1"+row_1);
        System.out.print("column"+column_1);
        int row_2=B[0].length;
        int column_2=B.length;
        System.out.println("row_1"+row_2);
        System.out.println("column"+column_2);
        int C[][]=new int[row_1][column_2];
        int count=0;
        for(int i=0;i<row_1;i++)
        {
            for(int j=0;j<column_2;j++)
            {
              for(int k=0;k<row_2;k++)
              {
                C[i][j]+=A[i][k]*B[k][j];
                count++;
              }
            }
        }
        System.out.print(count);
        return C;

    }
    public static void main(String[] args)
    {
        Scanner sc=new Scanner(System.in);
        int i=0,j=0;
        int row_1=sc.nextInt();
        int column_1=sc.nextInt();
        int row_2=sc.nextInt();
        int column_2=sc.nextInt();
        int A[][]=new int[row_1][column_1];
        int B[][]=new int[row_2][column_2];
        for( i=0;i<row_1;i++)
        {
            for(j=0;j<column_1;j++)
            {
                A[i][j]=sc.nextInt();
            }
        }
        for( i=0;i<row_2;i++)
        {
            for(j=0;j<column_2;j++)
            {
                B[i][j]=sc.nextInt();
            }
        }
        sc.close();
        printMatrix(multiply(A, B),row_1,column_2);

    }
}