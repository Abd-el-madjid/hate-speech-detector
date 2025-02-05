import React from "react";
import { Menu } from "antd";
import { HomeOutlined, FileTextOutlined } from "@ant-design/icons";
import { Link } from "react-router-dom";

const Sidebar = () => (
  <Menu theme="dark" mode="inline">
    <Menu.Item key="1" icon={<HomeOutlined />}>
      <Link to="/">Home</Link>
    </Menu.Item>
    <Menu.Item key="2" icon={<FileTextOutlined />}>
      <Link to="/report">Report</Link>
    </Menu.Item>
  </Menu>
);

export default Sidebar;
