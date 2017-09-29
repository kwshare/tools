
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
 * @author Benny~
 */
public class OnekeySnapshot {

    private static String secretID = "Your secretID";
    private static String secretKey = "Your secretKey";
    private static String Region = "Your Region";
    private static String diskID = "Your diskID";
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
        //Magic snapshot name
        String[] fortune = {"I miss you", "I missed you", "Exodus", "I flipped", "Nothing will ever compare",
                "Remember me", "Benny with Moon"};
        params.put("snapshotName", fortune[(int) (Math.random() * 7)]);

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
        //查询快照，存储旧的snapshotID,并删除旧快照
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
            //取得最旧的快照ID

            SnapshotID = json_result.getJSONArray("snapshotSet").getJSONObject(0).getString("snapshotId");
            //删除最旧的快照
            params.clear();
            params.put("limits", 3);
            params.put("snapshotIds.0", SnapshotID);
            result = module.call("DeleteSnapshot", params);
            json_result = new JSONObject(result);
            System.out.println("删除最旧一个快照中..." + json_result.getString("codeDesc"));

        } catch (Exception e) {
            System.out.println("error..." + e.getMessage());
        }

    }

}
