import React, { useState, useEffect } from "react";
import {
  Card,
  Tabs,
  Button,
  Typography,
  Row,
  Col,
  Space,
  Progress,
  Divider,
  Select,
  Spin,
  Table,
} from "antd";
import axios from "axios";

import ModelChart from "../components/ModelStatistics/ModelChart";
import ConfusionMatrix from "../components/ModelStatistics/ConfusionMatrix";
import LabelDistribution from "../components/ModelStatistics/LabelDistribution";

const { Title } = Typography;
const { TabPane } = Tabs;
const { Option } = Select;

const ModelStatistics = () => {
  const [activeTab, setActiveTab] = useState("1");
  const [modelStats, setModelStats] = useState({
    accuracy: 0,
    f1Score: 0,
    confusionMatrix: [],
    inferenceTime: 0,
    avgInferenceTime: 0,
    classDistribution: {},
    predictionDistribution: {},
  });
  const [datasets, setDatasets] = useState([]);
  const [selectedDataset, setSelectedDataset] = useState(null);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    fetchUploadedDatasets();
  }, []);

  // Fetch datasets
  const fetchUploadedDatasets = async () => {
    setLoading(true);
    try {
      const response = await axios.get("http://localhost:5000/datasets");
      setDatasets(response.data);
    } catch (error) {
      console.error("Error fetching datasets:", error);
    } finally {
      setLoading(false);
    }
  };

  // Fetch model statistics
  const fetchModelStatistics = async () => {
    if (!selectedDataset) {
      console.error("No dataset selected");
      return;
    }

    setLoading(true);
    try {
      const response = await axios.get(
        `http://localhost:5000/model-statistics?dataset=${selectedDataset}`
      );
      const {
        accuracy,
        f1_score,
        confusion_matrix,
        inference_time,
        avg_inference_time_per_sample,
        class_distribution,
        prediction_distribution,
      } = response.data;

      setModelStats({
        accuracy: (accuracy * 100).toFixed(2),
        f1Score: (f1_score * 100).toFixed(2),
        confusionMatrix: confusion_matrix,
        inferenceTime: inference_time,
        avgInferenceTime: avg_inference_time_per_sample,
        classDistribution: class_distribution,
        predictionDistribution: prediction_distribution,
      });
      console.log(modelStats.classDistribution);
      console.log(modelStats.predictionDistribution);
    } catch (error) {
      console.error("Error fetching model statistics:", error);
    } finally {
      setLoading(false);
    }
  };

  const handleDatasetChange = (value) => {
    setSelectedDataset(value);
  };

  const handleFileUpload = async (event) => {
    const file = event.target.files[0];
    if (!file) return;

    const formData = new FormData();
    formData.append("dataset", file);

    setLoading(true);

    try {
      await axios.post("http://localhost:5000/upload_dataset", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });
      fetchUploadedDatasets();
    } catch (error) {
      console.error("Error uploading dataset:", error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <Row
        justify="space-between"
        align="middle"
        style={{ padding: "20px 24px" }}
      >
        <Title level={2} style={{ margin: 0 }}>
          Hate Speech Model Statistics
        </Title>
        <Space>
          <input
            type="file"
            style={{ display: "none" }}
            id="file-upload"
            onChange={handleFileUpload}
          />
          <Button
            style={{ marginRight: 8 }}
            onClick={() => document.getElementById("file-upload").click()}
          >
            Import Data
          </Button>
          <Select
            value={selectedDataset}
            style={{ width: 200 }}
            onChange={handleDatasetChange}
            placeholder="Select Dataset"
          >
            {datasets.map((dataset) => (
              <Option key={dataset} value={dataset}>
                {dataset}
              </Option>
            ))}
          </Select>
          <Button type="primary" onClick={fetchModelStatistics}>
            Evaluate
          </Button>
        </Space>
      </Row>

      <Divider style={{ padding: 10 }} />

      <Spin spinning={loading} tip="Loading...">
        <Row gutter={[16, 16]}>
          <Col span={8}>
            <Card title="Accuracy">
              {modelStats.accuracy}%
              <Progress percent={modelStats.accuracy} />
            </Card>
          </Col>
          <Col span={8}>
            <Card title="F1 Score">
              {modelStats.f1Score}%
              <Progress percent={modelStats.f1Score} />
            </Card>
          </Col>
          <Col span={8}>
            <Card title="Inference Time">
              Total: {modelStats.inferenceTime.toFixed(2)} seconds
              <Divider />
              Avg per sample: {modelStats.avgInferenceTime.toFixed(4)} seconds
            </Card>
          </Col>
        </Row>

        <Card style={{ marginTop: "20px" }}>
          <Tabs defaultActiveKey="1" onChange={(key) => setActiveTab(key)}>
            {/* <TabPane tab="Cost History" key="1">
              <ModelChart data={modelStats.costHistory} />
            </TabPane> */}
            <TabPane tab="Confusion Matrix" key="2">
              <ConfusionMatrix matrix={modelStats.confusionMatrix} />
            </TabPane>
            <TabPane tab="Class Distribution" key="3">
              <LabelDistribution matrix={modelStats.classDistribution} />
            </TabPane>
            <TabPane tab="Prediction Distribution" key="4">
              <LabelDistribution
                directoryData={modelStats.predictionDistribution}
              />
            </TabPane>
          </Tabs>
        </Card>
      </Spin>
    </div>
  );
};

export default ModelStatistics;
