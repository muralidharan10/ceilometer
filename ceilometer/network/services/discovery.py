# -*- encoding: utf-8 -*-
#
# Copyright © 2014 Cisco Systems, Inc
#
# Author:Pradeep Kilambi <pkilambi@cisco.com>
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from ceilometer import neutron_client
from ceilometer import plugin


class _BaseServicesDiscovery(plugin.DiscoveryBase):

    def __init__(self):
        super(_BaseServicesDiscovery, self).__init__()
        self.neutron_cli = neutron_client.Client()


class LBPoolsDiscovery(_BaseServicesDiscovery):

    def __init__(self):
        super(LBPoolsDiscovery, self).__init__()

    def discover(self, param=None):
        """Discover resources to monitor."""

        pools = self.neutron_cli.pool_get_all()
        return [i for i in pools
                if i.get('status') != 'error']


class LBVipsDiscovery(_BaseServicesDiscovery):

    def __init__(self):
        super(LBVipsDiscovery, self).__init__()

    def discover(self, param=None):
        """Discover resources to monitor."""

        vips = self.neutron_cli.vip_get_all()
        return [i for i in vips
                if i.get('status', None) != 'error']


class LBMembersDiscovery(_BaseServicesDiscovery):

    def __init__(self):
        super(LBMembersDiscovery, self).__init__()

    def discover(self, param=None):
        """Discover resources to monitor."""

        members = self.neutron_cli.member_get_all()
        return [i for i in members
                if i.get('status', None) != 'error']


class LBHealthMonitorsDiscovery(_BaseServicesDiscovery):

    def __init__(self):
        super(LBHealthMonitorsDiscovery, self).__init__()

    def discover(self, param=None):
        """Discover resources to monitor."""

        probes = self.neutron_cli.health_monitor_get_all()
        return probes


class VPNServicesDiscovery(_BaseServicesDiscovery):

    def __init__(self):
        super(VPNServicesDiscovery, self).__init__()

    def discover(self, param=None):
        """Discover resources to monitor."""

        vpnservices = self.neutron_cli.vpn_get_all()
        return [i for i in vpnservices
                if i.get('status', None) != 'error']


class IPSecConnectionsDiscovery(_BaseServicesDiscovery):

    def __init__(self):
        super(IPSecConnectionsDiscovery, self).__init__()

    def discover(self, param=None):
        """Discover resources to monitor."""

        conns = self.neutron_cli.ipsec_site_connections_get_all()
        return conns


class FirewallDiscovery(_BaseServicesDiscovery):

    def __init__(self):
        super(FirewallDiscovery, self).__init__()

    def discover(self, param=None):
        """Discover resources to monitor."""

        fw = self.neutron_cli.firewall_get_all()
        return [i for i in fw
                if i.get('status', None) != 'error']


class FirewallPolicyDiscovery(_BaseServicesDiscovery):

    def __init__(self):
        super(FirewallPolicyDiscovery, self).__init__()

    def discover(self, param=None):
        """Discover resources to monitor."""

        return self.neutron_cli.fw_policy_get_all()
