import React from "react";
import {
  Tabs,
  Button,
  Typography,
  Row,
  Col,
  Space,
  Divider,
  Progress,
  Card,
} from "antd";

import NewDetection from "../components/tabs/NewDetection";
import History from "../components/tabs/History";

const { TabPane } = Tabs;
const { Title } = Typography;
const WaveIcon = () => (
  <svg
    width="16"
    height="16"
    viewBox="0 0 24 24"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
  >
    <path
      d="M3 12h1m4-2v4m4-8v12m4-10v8m4-6v4"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    />
  </svg>
);
const Report = () => (
  <div style={{ padding: "20px" }}>
    <Row
      justify="space-between"
      align="middle"
      style={{ padding: "20px 24px" }}
    >
      <Title level={2} style={{ margin: 0 }}>
        Hate Speech Model report
      </Title>
      <Space>
        <Button style={{ marginRight: 8 }} icon={<WaveIcon />}>
          Voice
        </Button>
      </Space>
    </Row>

    <Tabs defaultActiveKey="1">
      <TabPane tab="New Detection" key="1">
        <NewDetection />
      </TabPane>
      <TabPane tab="History" key="2">
        <History />
      </TabPane>
    </Tabs>
  </div>
);

export default Report;
