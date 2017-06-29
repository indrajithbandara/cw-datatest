
import java.util.Iterator;
import java.util.concurrent.ConcurrentLinkedQueue;

import org.apache.commons.lang.math.NumberUtils;
import org.apache.log4j.Logger;

import com.datong.pear.system.common.Constants;
import com.datong.pear.system.common.Result;

/**
 * 活动登记队列
 *
 * @author jqlin
 */
public class TicketQueue {
    private static ConcurrentLinkedQueue<ActivityRecordModel> linkedQueue = new ConcurrentLinkedQueue<ActivityRecordModel>();
    
    private static final Logger logger = Logger.getLogger(TicketQueue.class);
    
    public static boolean isRunning = false;
    
    /**
     * 活动登记对象放入队列中
     * 
     * @param activityRecord
     * @author jqlin
     */
    public static void offer(ActivityRecordModel activityRecord) {
        if(activityRecord == null){
            logger.info(String.format("%s activityRecord is null", TicketQueue.class.getName()));
            return;
        }
        
        if(NumberUtils.toLong(activityRecord.getId(), 0) == 0L){
            logger.info(String.format("%s activityRecord.id is illegal，activityRecord.id=%s",
                    TicketQueue.class.getName(), activityRecord.getId()));
            return;
        }
        
        logger.info(String.format("%s 即将放入队列的活动登记信息：%s", TicketQueue.class.getName(), activityRecord));
        if(activityRecord.getState() != Constants.ActivityRecordStatus.WPF){
            logger.info(String.format("%s activityRecordId=%s 状态不是未派发，无法放入队列", TicketQueue.class.getName(), activityRecord.getId()));
            return;
        }
        
        logger.info(String.format("%s activityRecordId=%s 准备放入队列", TicketQueue.class.getName(), activityRecord.getId()));
        linkedQueue.offer(activityRecord);
        logger.info(String.format("----setActivityRecordId=%s *****", activityRecord.getId()));
        logger.info(String.format("%s activityRecordId=%s 放入队列成功", TicketQueue.class.getName(), activityRecord.getId()));
        logger.info("**********************************************************************");
    }

    /**
     * 从队列中获取活动登记对象，并派券
     * 
     * @return
     * @author jqlin
     */
    public static synchronized void pollAndSendTicket(TicketService ticketService) {
        isRunning = true;
        
        logger.info("准备从队列中获取活动登记对象，并派券...");
        if(linkedQueue != null && !linkedQueue.isEmpty()){ 
            ActivityRecordModel activityRecordModel = null;
            while (true) {
                Iterator<ActivityRecordModel> arIterator = linkedQueue.iterator();
                if(!arIterator.hasNext()){
                    try {
                        Thread.sleep(1000);
                    } catch (InterruptedException e) {
                        logger.info("队列派券异常中断");
                    }
                    
                    continue;
                } 
                
                activityRecordModel = arIterator.next();
                logger.info(String.format("----getActivityRecordId=%s， Thread=%s *****", activityRecordModel.getId(), Thread.currentThread().getId()));
                logger.info(String.format("%s 从队列中获取的活动登记信息：%s", TicketQueue.class.getName(), activityRecordModel));
                
                logger.info(String.format("%s activityRecordId=%s 准备移出队列", TicketQueue.class.getName(), activityRecordModel.getId()));
                linkedQueue.remove(activityRecordModel);
                logger.info(String.format("%s activityRecordId=%s 移出队列成功", TicketQueue.class.getName(), activityRecordModel.getId()));
                
                logger.info(String.format("%s activityRecordId=%s 队列派券开始", TicketQueue.class.getName(), activityRecordModel.getId()));
                Result result = ticketService.sendTicket(activityRecordModel);
                logger.info(String.format("%s 活动登记派券接口返回信息：", TicketQueue.class.getName()));
                logger.info(result);
                logger.info(String.format("%s 活动登记派券结束", TicketQueue.class.getName()));
                
                logger.info("**********************************************************************");
            }
        } else {
            logger.info("队列中活动登记对象为空，没有数据可派券...");
        }
        
        isRunning = false;
    }
}