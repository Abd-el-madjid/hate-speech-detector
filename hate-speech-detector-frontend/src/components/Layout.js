import React from "react";
import { Layout } from "antd";
import Sidebar from "./Sidebar";

const { Sider, Content } = Layout;

const MainLayout = ({ children }) => (
  <Layout style={{ minHeight: "100vh" }}>
    {/* Sidebar: Fixed */}
    <Sider width={200} style={{ position: "fixed", height: "100vh", left: 0 }}>
      <Sidebar />
    </Sider>

    {/* Content Area: Scrollable */}
    <Layout style={{ marginLeft: 200 }}>
      <Content
        style={{
          padding: "24px",
          margin: "16px 0",
          background: "#fff",
          overflowY: "auto", // Makes content scrollable
          height: "calc(100vh - 64px)", // Adjust the content height to fill the remaining space
        }}
      >
        {children}
      </Content>
    </Layout>
  </Layout>
);

export default MainLayout;
