public class Search {
    public class BiTreeNode{
        int m_nValue;
        BiTreeNode m_pLeft;
        BiTreeNode m_pRight;
        
    }
    //顺序查找，查到则返回该值下标，查不到返回-1.
    public int SequenceSearch(int[] a,int b){
        if(a==null)
            return -1;
        for(int i=0;i<a.length;i++){
            if(a[i]==b)
                return i;
        }
        return -1;
    }
    //折半查找，二分查找,要求查找的数组是有序的。只适合于静态查找。
    public int BinarySearch(int[] a,int b){
        if(a==null)
            return -1;
        int low=0;
        int high=a.length-1;
        while(low<=high){
            int middle=(low+high)/2;
            if(a[middle]==b)
                return middle;
            if(a[middle]<b)
                low=middle+1;
            else
                high=middle-1;
        }
        return -1;
    }
    //折半查找的递归算法
    public int BinarySearch1(int[] a,int b,int low,int high){
        if(a==null||low>high)
            return -1;
        int middle=(low+high)/2;
        if(a[middle]==b)
            return middle;
        if(a[middle]<b)
            return BinarySearch1(a,b,middle+1,high);
        else
            return BinarySearch1(a,b,low,middle-1);
    }
    //二叉排序树，二叉查找树，二查搜索树，是一颗具有如下特点的树，树的左边都比它小，树的右边都比它大。
    public BiTreeNode BinaryBiSearch(BiTreeNode pHead,int b){
        if(pHead==null)
            return null;
        if(pHead.m_nValue==b)
            return pHead;
        if(pHead.m_pLeft!=null)
            return BinaryBiSearch(pHead.m_pLeft,b);
        if(pHead.m_pRight!=null)
            return BinaryBiSearch(pHead.m_pRight,b);
        return null;
    }
    public static void main(String[] args){
        int[] a={1,2,3,5,7,8,10};
        Search search=new Search();
        
        int i=search.BinarySearch(a,1);
        int k=search.BinarySearch1(a, 3,0,a.length-1);
        int j=search.SequenceSearch(a, 3);
        System.out.println(i+" "+j+" "+k);
    }
}