importstatic org.junit.Assert.*;
importstatic org.hamcrest.Matcher.*;

import org.junit.Test;
import com.junit4.cc.*;

import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.AfterClass;
import org.junit.After;
import org.junit.Ignore;


public class TTest {
    
    @BeforeClass  //的所有方法运行之前运行。
public static void beforeClass(){
        System.out.println("------------beforeClass");
    }
    
    @AfterClass   //在所有方法运行之后运行
public static void afterClass(){
        System.out.println("-------------afterClass");
    }
    
    @Before   //每个测试方法运行之前运行
public void before(){
        System.out.println("=======before");
    }
    
    @After   //每个测试方法运行之后运行
public void after(){
        System.out.println("=======after");
    }

    @Test
    public void testAdd() {
        int z=new T().add(5,3);
        assertEquals(8,z);
        System.out.println("test Run through");
    }
    
    @Test ()
    public void testdivision(){
              System.out.println("in Test Division");

    }

    @Ignore   //表示这个方法是不被运行的
    @Test
    (expected=java.lang.ArithmeticException.class,timeout=100) //timeout表示要求方法在100毫秒内运行完成，否则报错
public void testDivide(){
        int z =new T().divide(8,2);
    }
    
    

}