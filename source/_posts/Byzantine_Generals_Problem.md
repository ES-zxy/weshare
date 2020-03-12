title: Byzantine Generals Problem
author: zxy
tags:
  - DISTRIBUTED
  - ALGORITHM
  - CONSENSUS MECHANISM
categories:
  - Algorithm
date: 2020-03-12 13:24:00
---
## 背景信息
> 维基百科
拜占庭将军问题（Byzantine Generals Problem），是由莱斯利·兰波特在其同名论文中提出的分布式对等网络通信容错问题。

在分布式计算中，不同的计算机通过通讯交换信息达成共识而按照同一套协作策略行动。但有时候，系统中的成员计算机可能出错而发送错误的信息，用于传递信息的通讯网络也可能导致信息损坏，使得网络中不同的成员关于全体协作的策略得出不同结论，从而破坏系统一致性。拜占庭将军问题被认为是容错性问题中最难的问题类型之一。

## 问题描述
莱斯利·兰波特在其论文中描述了如下问题：

一组拜占庭将军分别各率领一支军队共同围困一座城市。为了简化问题，将各支军队的行动策略限定为进攻或撤离两种。因为部分军队进攻部分军队撤离可能会造成灾难性后果，因此各位将军必须通过投票来达成一致策略，即所有军队一起进攻或所有军队一起撤离。因为各位将军分处城市不同方向，他们只能通过信使互相联系。在投票过程中每位将军都将自己投票给进攻还是撤退的信息通过信使分别通知其他所有将军，这样一来每位将军根据自己的投票和其他所有将军送来的信息就可以知道共同的投票结果而决定行动策略。

## BFT协议

## Raft协议
在系统不同的机器之间会传递错误的消息，这种情况即为拜占庭问题。这与”网络分割、机器崩溃...”是不同的。比如Raft协议不能容忍拜占庭问题，但是能够在非拜占庭错误情况下，有网络延迟、分区、丢包、冗余和乱序等错误情况出现时，都可以保证其操作的正确性。

### Raft Leader选举


## 相关算法
1980年代被提出用来达到拜占庭容错的架构，如：FTMP、MMFCS与 SIFT。
1999年，卡斯托（Miguel Castro）与李斯克夫（Barbara Liskov）提出了实用拜占庭容错（PBFT）演算法[9]。该演算法能提供高效能的运算，使得系统可以每秒处理成千的请求，比起旧式系统快了一些。
而在PBFT之后，许多用于拜占庭容错（BFT）的通讯协议也被提出来改善其通讯的强健性与效率。比如Q/U、HQ、Zyzzyva与ABsTRACTs，用来提升效率。而Aardvark与RBFT是用来加强强健性。另外，Adapt则使用原有的BFT协议做调适，以强化其效率与强健性。BFT协议更可以借由加入可任务的单元，以减少发出副本的次数。比如：A2M-PBFT-EA[17]与MinBFT。
在对等式数位货币系统比特币里，比特币网路的运作是平行的（parallel）。各节点与终端都运算著区块链来达成工作量证明（PoW）。


## Reference
[《In Search of an Understandable Consensus Algorithm (Extended Version)》](https://ramcloud.atlassian.net/wiki/download/attachments/6586375/raft.pdf)
[拜占庭将军问题-维基百科](https://zh.wikipedia.org/zh-hans/%E6%8B%9C%E5%8D%A0%E5%BA%AD%E5%B0%86%E5%86%9B%E9%97%AE%E9%A2%98)
[什么是拜占庭将军问题](https://learnblockchain.cn/2018/02/05/bitcoin-byzantine/)
[如何理解拜占庭将军问题](https://www.zhihu.com/question/23167269)
