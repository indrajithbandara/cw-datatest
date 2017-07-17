import java.util.Random;

public class Sort {

    public Sort() {
        // TODO Auto-generated constructor stub
    }

    // 冒泡排序，该排序总共要进行n-1趟，每一趟的比较次数递减
    public void bubbleSort(int[] a) {
        if (a == null) {
            return;
        }
        int len = a.length;
        for (int i = 0; i < a.length - 1; i++)
            for (int j = 0; j < len - i - 1; j++) {
                if (a[j] > a[j + 1])
                    swrap(a, j, j + 1);
            }

    }

    // 直接插入排序，该排序首先要设置一个哨兵，因为在排序的时候向前比较的过程中不会越界，a<a,不可能成立。
    public void insertSort(int[] a) {
        if (a == null) {
            return;
        }
        int len = a.length;
        int[] b = new int[len + 1];
        System.arraycopy(a, 0, b, 1, len);
        for (int i = 2; i <= len; i++) {
            b[0] = b[i];
            for (int j = i - 1; j > 0; j--) {
                if (b[j] > b[0]) {
                    b[j + 1] = b[j];// 元素后移一位
                    b[j] = b[0];
                }
            }
        }
        System.arraycopy(b, 1, a, 0, len);
    }

    // shell排序，该排序是插入排序的一种，只是，间隔不再是1而是d
    public void shellSort(int[] a) {
        if (a == null)
            return;
        int len = a.length;
        int[] b = new int[len + 1];
        System.arraycopy(a, 0, b, 1, len);
        for (int d = len / 2; d >= 1; d /= 2) {
            for (int i = d + 1; i <= len; i++) {
                b[0] = b[i];
                for (int j = i - d; j > 0; j -= d) {
                    if (b[j] > b[0]) {
                        b[j + d] = b[j];
                        b[j] = b[0];
                    }
                }
            }
        }
        System.arraycopy(b, 1, a, 0, len);
    }

    // 选择排序,选出最小的值查到整个排好序的数组中,只要进行n-1次选择就OK
    public void selectSort(int[] a) {
        if (a == null)
            return;
        int len = a.length;
        for (int i = 0; i < len - 1; i++) {
            int min = i;// 初始化最小元素的下标。
            for (int j = i + 1; j < len; j++) {
                if (a[j] < a[min]) {
                    min = j;// 选出最小元素的下标。
                }
                swrap(a, i, min);

            }
        }
    }

    // 快速排序一次排序的结果，index左边的值小于它，右边的值大于它
    public int parition(int[] a, int start, int end) {
        Random rand = new Random();
        int index = start + rand.nextInt(end - start);
        swrap(a, index, end);
        int small = start - 1;
        for (index = start; index < end; index++) {
            if (a[index] < a[end]) {
                small++;
                if (small != index) {
                    swrap(a, small, index);
                }
            }
        }
        small++;
        swrap(a, small, end);
        return small;
    }

    // 快速排序，通过快速排序一趟的排序来确定index值，然后递归排序。
    public void quickSort(int[] a, int start, int end) {
        if (a == null || start < 0 || end > a.length || start == end)
            return;
        int index = parition(a, start, end);
        if (index > start)
            quickSort(a, start, index - 1);
        if (index < end)
            quickSort(a, index + 1, end);
    }

    // 堆排序，首先要构建堆，我们以大根堆为例，就是大根堆的左右子节点都比本身要小
    public void heapSort(int[] a) {
        if (null != a) {
            int end = a.length - 1;
            for (int i = (end - 1) / 2; i >= 0; i--)
                adjustHead(a, i, end);
            for (int i = end; i >= 0; i--) {
                swrap(a, 0, i);
                adjustHead(a, 0, i - 1);
            }
        }
    }

    public void adjustHead(int[] a, int start, int end) {
        if (a == null || start < 0 || end > a.length || start == end)
            return;
        int temp = a[start];
        for (int i = 2 * start + 1; i <= end; i = i * 2 + 1) {
            if (i < end && a[i] < a[i + 1])
                i++;
            if ((a[i] > temp)) {
                a[start] = a[i];
                start = i;
            } else
                break;
        }
        a[start] = temp;
    }

    private void swrap(int[] a, int j, int i) {
        // TODO Auto-generated method stub
        int temp = a[j];
        a[j] = a[i];
        a[i] = temp;
    }

    private void print(int[] a) {
        for (int temp : a)
            System.out.print(temp + " ");
        System.out.println();
    }
    //归并排序，首先将数组分成n个小片，然后两两归并。需要借助一个O（n）的空间。
        //时间复杂度为O（nlogn）
       public void mergeSort(int[] a){
           if(a==null)
               return;
           int[] b=new int[a.length];
           System.arraycopy(a, 0, b, 0, a.length);
           mergeSortCore(a,b,0,a.length-1);
           System.arraycopy(b, 0, a, 0, a.length);
          
       }
       //归并排序的核心
       public void mergeSortCore(int[] a, int[] b, int start, int end) {
           if(a==null||b==null){
               return;
           }
           if(start==end){
               b[start]=a[start];
               return;
           }
           int len=(end-start)/2;
           mergeSortCore(b,a,start,start+len);
           mergeSortCore(b,a,start+len+1,end);
           //用来表示前半段的最后一个下标
           int i=start+len;
           //用来表示后半段的最后一个下标
           int j=end;
           int index=end;
           while(i>=start&&j>=start+len+1){
               if(a[i]>a[j])
                   b[index--]=a[i--];
               else
                   b[index--]=a[j--];
                   
           }
           for(;i>=start;i--)
               b[index--]=a[i];
           for(;j>=start+len+1;j--)
               b[index--]=a[j];
           
           
       }

    public static void main(String[] args) {
        int[] a = { 3, 5, 7, 2, 1, 8, 4 };
        Sort s = new Sort();
        s.bubbleSort(a);
        s.print(a);
        s.insertSort(a);
        s.print(a);
        s.shellSort(a);
        s.print(a);
        s.selectSort(a);
        s.print(a);
        s.quickSort(a, 0, a.length - 1);
        s.print(a);
        s.heapSort(a);
        s.print(a);
    }

}