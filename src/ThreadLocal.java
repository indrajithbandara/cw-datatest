public class ThreadLocal<T> {  
    protected T initialValue() {  
        return null;  
    }  
    public ThreadLocal() {  
    }  
    public T get() {  
        Thread t = Thread.currentThread();  
        ThreadLocalMap map = getMap(t);  
        if (map != null) {  
            ThreadLocalMap.Entry e = map.getEntry(this);  
            if (e != null)  
                return (T)e.value;  
        }  
        return setInitialValue();  
    }  
    private T setInitialValue() {  
        T value = initialValue();  
        Thread t = Thread.currentThread();  
        ThreadLocalMap map = getMap(t);  
        if (map != null)  
            map.set(this, value);  
        else  
            createMap(t, value);  
        return value;  
    }  
    public void set(T value) {  
        Thread t = Thread.currentThread();  
        ThreadLocalMap map = getMap(t);  
        if (map != null)  
            map.set(this, value);  
        else  
            createMap(t, value);  
    }  
     public void remove() {  
         ThreadLocalMap m = getMap(Thread.currentThread());  
         if (m != null)  
             m.remove(this);  
     }  
    ThreadLocalMap getMap(Thread t) {  
        return t.threadLocals;  
    }  
    void createMap(Thread t, T firstValue) {  
        t.threadLocals = new ThreadLocalMap(this, firstValue);  
    }  
}  