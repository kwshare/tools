
import com.qcloud.Module.Snapshot;
import com.qcloud.QcloudApiModuleCenter;
import com.qcloud.Utilities.Json.JSONObject;
import java.util.TreeMap;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
/**
 *
 * @author Benny~
 */
public class OnekeySnapshot {

    private static String secretID = "AKIDU---EQgAgQ2";
    private static String secretKey = "nV2OY---qqkmi";
    private static String Region = "sh";
    private static String diskID = "disk-ixath";
    private static String SnapshotID = null;

    public static void main(String[] args) {

        processSnapShot();
        createSnapShot();
    }

    private static void createSnapShot() {
        //创建快照
        TreeMap<String, Object> config = new TreeMap<String, Object>();
        config.put("SecretId", secretID);
        config.put("SecretKey", secretKey);
        config.put("RequestMethod", "GET");
        config.put("DefaultRegion", Region);
        QcloudApiModuleCenter module = new QcloudApiModuleCenter(new Snapshot(),
            config);
        TreeMap<String, Object> params = new TreeMap<String, Object>();
        params.put("limits", 3);
        params.put("storageId", diskID);

        //System.out.println(module.generateUrl(Action,params));
        String result = null;
        try {
            result = module.call("CreateSnapshot", params);
            JSONObject json_result = new JSONObject(result);
            System.out.println("创建新的快照中..." + json_result.getString("codeDesc"));

        } catch (Exception e) {
            System.out.println("error..." + e.getMessage());
        }

    }

    private static void processSnapShot() {
        //查询快照，存储上一个的snapshotID,并删除上一个快照
        TreeMap<String, Object> config = new TreeMap<String, Object>();
        config.put("SecretId", secretID);
        config.put("SecretKey", secretKey);
        config.put("RequestMethod", "GET");
        config.put("DefaultRegion", Region);
        QcloudApiModuleCenter module = new QcloudApiModuleCenter(new Snapshot(),
            config);
        TreeMap<String, Object> params = new TreeMap<String, Object>();//instanceIds.0
        params.put("limits", 3);
        params.put("storageId", diskID);

        //System.out.println(module.generateUrl("describeSnapshot",params));
        String result = null;
        try {
            result = module.call("DescribeSnapshots", params);
            JSONObject json_result = new JSONObject(result);
            //取得最后一个快照的ID          
            SnapshotID = json_result.getJSONArray("snapshotSet").getJSONObject(json_result.getInt("totalCount") - 1).getString("snapshotId");
            //删除最后一个快照
            params.clear();
            params.put("limits", 3);
            params.put("snapshotIds.0", SnapshotID);
            result = module.call("DeleteSnapshot", params);
            json_result = new JSONObject(result);
            System.out.println("删除最后一个快照中..." + json_result.getString("codeDesc"));

        } catch (Exception e) {
            System.out.println("error..." + e.getMessage());
        }

    }

}
