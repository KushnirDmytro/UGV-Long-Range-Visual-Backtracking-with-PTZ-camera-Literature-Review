# Content Structure draft

## Introduction: Motivation for the topic

(+Here compile those from the typical papers, used in the literature list.)
Lack of open systematic tools that are stopping the advancement of the field. Argiculture, mining, milteck, and other industries are in need of the technology and are impacted by the lack of the open-source tools.

## Methodology: How you collected and analyzed the literature

*about the snowballing tool and the search in the Google Scholar and other sources.
*about good pattern in the field: in comparison to the general CS, the Robotics field has better culture of large, well structured field reviews dedicated to specific aspects, tools, equipment... There are even kind of yearly almanacs, that are dedicated to the specific aspects of the field. (TODO: rephrase and add meta-research about the topic)

- How I analyzed and build the solutions based on MeROS and structured analysis going "Task-Requirment-Design-Implementation-Validation" way. (Taks-Requirement-Analisys-Design... the related works and field analysis are the part of Analysis-Design steps)
<https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3285286> -- interesting note about explosive dosruptions from the technologies in the field of robotics (as Kinect was). I think that MeROS and blossom of ROS2 can contribute to similar effect.

Note: mention organized challanges-based research, like DARPA. Here can amplify the distinctive nature of the Robotics Research

- TODO: include the MeROS diagrams of the requirements allocation and the Design <<allocation>>
- TODO: "Layers" on the diagram of requirements to show the iterative implamentation plan

## State-of-the-Art: Subsections for different aspects, like mapping approaches, visual perception

- About the PTZ camera and the importance of the technology for the UGVs.
- About the importance of the modular design and the requirement-based design. MeROS
- Clain that SOTA is often closed and platfrom-locked, so we have "public" SOTA and lots of "private" SOTA examples. Academy also uses purchased platforms and vendor-locked equipment, so reproducibility is in crysis and we have public-SOTA halt. [TODO: am I invented Publlic SOTA term? Dig it! ] About the importance of the open-source tools and the open-source hardware platforms for the technology advancement. Example of the Zoom cameras callibration, Raspberry Pi, ROS philosophy and the MeROS project.

## Research Gaps: Highlight areas for improvement or new explorations

### Identification via Task-Requirment-Design-Implementation-Validation analysis

### (?) Modularity and the requirement-based design. - one of the targets of this research

    We are formulating the requirements list for the UGV platform and validate them in practice. Some risk and related topics (as platform path planning) and interfacing questions are also explored in the process, because those sytems cary the risk of the failure or can be reused in Arianda module.

### Main research gaps

- About PTZ camera incorporation.
- Long-range navigation in unstructured environments extension.
- Explitation of the Encapsulated software-hardware module, independent from the general (UGV) platform
  - Problem relaxations: "backtracking" setup
- Interfacing with different UGV platforms. Requirements management. Building platform-independent solutions
- Main sensor: PTZ camera. Callibration and processing. Limitations of open-source tools for ISP and callibration
  - Alternative solutions exploration: 360 camera, other camera configurations

### Connected constraints exploration

those are list of the problems that are connected to the main research gap and are crucial for the technology advancement

    - Planning and power budgeting
    - Environemtal limitations: weather, light, fog, traversibility complexity, critical environment changes, existance of the landmarks.
    - Scalability and the real-time processing requirements
    - Integration with the ROS-based platform and the other interfaces

## Conclusion and Motivation: Refine why your research challenge matters

- Importance of "Modular design" and refinement of requirements for potential other UGV platforms that can use technology/Arianda module.
- Identification of the crucial bottlenecks that are halting the advancement of the field.
- Steps to check the feasibility of adressing the bottlenecks:
  - Works on open-source digital camera callibration and processing asspects.
  - Works on the integration of the camera with the ROS platform.
  - Works on open platform solution to ensure the reproduction of the results and the integration of the technology in the other platforms.
  - Validation-by-implementation: (*MeROS philosophy)
    - Implementation of the
    - Validation on the real paltform of the technology integration scenario on the Husky UGV platform.
    - Maintanance of the clear comminication interfaces and MeROS documentation. This holds that the technology can be used by the other platforms, that can support given interfaces.
