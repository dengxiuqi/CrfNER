# CrfNER
#### 基于CRF的中文实体标注

#### 效果
迭代300次后各种标签在测试集上的评价指标:

             precision    recall  f1-score   support

      B-LOC       0.92      0.87      0.90      3658
      B-ORG       0.86      0.78      0.82      2185
      B-PER       0.96      0.86      0.90      1864
      I-LOC       0.89      0.87      0.88      4948
      I-ORG       0.89      0.84      0.86      8756
      I-PER       0.94      0.89      0.92      3601
          O       0.99      0.99      0.99    194185

    avg / total       0.98      0.98      0.98    219197
  
详情查看`Test.ipynb`文件
1. 例句  `英国首相鲍里斯·约翰逊表示，他在昨天晚上与美国白宫通电话，双方交流了抗击疫情的经验`  
    
        ('英', 'B-LOC'),('国', 'I-LOC')
        ('鲍', 'B-PER'),('里', 'I-PER'),('斯', 'I-PER'),('·', 'I-PER'),('约', 'I-PER'),('翰', 'I-PER'),('逊', 'I-PER')
        ('美', 'B-ORG'),('国', 'I-ORG'),('白', 'I-ORG'),('宫', 'I-ORG')
        
2. 例句  `李克强来到位于江西省赣州市于都县的梓山镇潭头村看望慰问群众`  
    
        ('李', 'B-PER'),('克', 'I-PER'),('强', 'I-PER')
        ('江', 'B-LOC'),('西', 'I-LOC'),('省', 'I-LOC')  
        ('赣', 'B-LOC'),('州', 'I-LOC'),('市', 'I-LOC')  
        ('于', 'B-LOC'),('都', 'I-LOC'),('县', 'I-LOC')  
        ('梓', 'B-LOC'),('山', 'I-LOC'),('镇', 'I-LOC')  
        ('潭', 'I-LOC'),('头', 'I-LOC'),('村', 'I-LOC')  

#### 工程结构

    CrfNER  
    ├── model   
    │　　└── ner.crfsuite 训练好的crf模型
    ├── data 数据集  
    │　　├── example.dev 验证集  
    │　　├── example.test 测试集
    │　　└── example.train 训练集
    ├── config.py 配置
    ├── utils.py 工具函数
    ├── train.py 训练模型
    └── Test.ipynb 效果测试