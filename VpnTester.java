import java.net.InetAddress;
import java.net.UnknownHostException;

public class VpnTester {
    public static void main(String[] args) {
        try {
            InetAddress originalAddress = InetAddress.getLocalHost();
            System.out.println("Original IP Address: " + originalAddress.getHostAddress());

            // Test VPN connection
            InetAddress vpnAddress = InetAddress.getLocalHost();
            System.out.println("VPN IP Address: " + vpnAddress.getHostAddress());
        } catch (UnknownHostException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
