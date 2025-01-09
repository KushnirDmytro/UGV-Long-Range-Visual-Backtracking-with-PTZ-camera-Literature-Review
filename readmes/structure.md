# Content Structure draft

## Introduction: Motivation for the topic

(+Here compile those from the typical papers, used in the literature list.)

- Importance of robotics research is obvious thing, but we have to say a few lines about it.
- Yet, there are limitations of innovation spread and drastic difference between the most developped robotics ecosystems and rest of the world.
Unlike with mainstream AI, where computation can be placed on remote cloud and researchers can work wherever they want the most tools are opensourced.
Robotics research and application scaling is lagging behind the mainstreem AI and general IT services.

TODO: why we want to see exactly the ground robotics?

Argiculture, mining, milteck, and other industries are in need of the technology and are impacted by the lack of the open-source tools.
Now Robotics advancements are fostered inside the techical giants. It is natural, but does not stop us fromt the wish to spread its benefits for the most indengered peoples. Ground robotics will have impact for agriculture -- giving people the nutritional security, it will have its impact in mining industries -- replacing the hardest and most dengerous jobs. In the context of hard and dangerous jobs the applications in the millitary field is uterrmost. It can help to protect the life and freadom for the nations. While the agressive regeems can afford to finance the large centralized wartime economies, the nations under thread are those, who are smaller and trying to foster their yound democratic societies. Thouse nations cannot outcompete miltech giants, the grass-roots democratic initative result in large amount of diverse robotic systems called to protect the nation. The limitations here are rather specific -- need of standartization : requirements, resources, ubiquity of open technologies... With this focus and mindset for democratization technological access for the future we are conducting this work.

Those factos are:
- Common apporach of acccessible design tools:
As UML once became one of the cornerstones of IT boom in software development, the SysML and, possibly MeROS will become the one of fruitfull branches of this tech.

- Hardware Opensource limitations:
Runnning ahead a bit we will talk about visual perception. OpenCV, started as the Intel project a long time ago, caused the explosion of CV.
Yet, the limitting part and price-bar-factor is the optics, which remains closed. We will touch those issues as example.

- Reusable tools:
TODO (GPT): whith which technology we can compare the ROS, ROS2? In general IT and AI fields I meant.

The ROS and ROS-based sensors are becomming one of the answers for the problems of open hardware limitations. You cam buy more "of the shelve" solutions and integrate them in the same system. You can balance your needs and budget and select from the diversity of equipment or even implement yuor own.

Lack of open systematic tools that are stopping the advancement of the field. *this is statement from one of the papers "conclusive part", closer to the end, work in agricultire. We can push of this as point of count. There professor concluded that ROS advancements can become the saving circle to boost the speed of research.


### Note: probably about problem statement we and wtf is Unstructured Environment we should talk here.

## Methodology: How you collected and analyzed the literature

### TODO: work on selection criteria (?)

- Existance of ROS implementation for the ground source.
- Use existing large-scale almanaics and the reviews in the field. (250+ papers for the review)
- There are plenty of available reviews. And aggregations of reviews maintained regularly. Use them.
- Use challenges and the DARPA-like research as the source of the relevant papers.
- Use methods that show the good performance in the benchmarks: S. Hausler, E. Griffiths, M. Ramezani, and P. Moghadam, “Towards long-term robotics in the wild,” arXiv preprint arXiv:2404.18477, 2024.
- Use the industry standards. There are few good-not-so-old ones.
<!-- The most stars on GIT -->

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
    Say, that we structure the review into main research gaps - the essential problems that we aim onto. They are accompanied with complexity relaxaction, that we are utilizing to iterate on working solutions that combine all of the critical components. Those relaxations and iterative improvements approach are also used as the ablation study kind of limitations.

### Main research gaps

- About PTZ camera incorporation.
- Long-range navigation in unstructured environments extension.
    - Places representation
    - Route followig between the Places
    -- As we aim to avoid the exact memoization, we will explore available solutioins for this problem or introduce the new one. This is crucial for the proposed topology-based navigation. We have to be able to explore and maintain the orientation between the landmarks.
    This is the limitation criterion: the better we have approach of the route following/path search, the less "Places" we have to memorize. This is the key to the long-range navigation in the unstructured environment. This is the key to the backtracking in the unstructured environment, important feature of the Arianda module.
    TODO: search for "boring road following" and "route following" in the literature.

- Explitation of the Encapsulated software-hardware module, independent from the general (UGV) platform
  - Problem relaxations: "backtracking" setup
- Interfacing with different UGV platforms. Requirements management. Building platform-independent solutions
- Main sensor: PTZ camera. Callibration and processing. Limitations of open-source tools for ISP and callibration
  - Alternative solutions exploration: 360 camera, other camera configurations

### Connected constraints exploration

those are list of the problems that are connected to the main research gap and are crucial for the technology advancement

- Planning and power budgeting
- Environemtal limitations: weather, light, fog, traversibility complexity, critical environment changes, existance of the landmarks.
- Motion control on Off-road terrains
- Scalability and the real-time processing requirements
    - Here we hold relaxation of real-time requirements
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

## NOTES

#### Datasets
- https://csiro-robotics.github.io/Wild-Places
- https://arxiv.org/html/2312.15364v2 -- Wild Scenes Dataset
S. Hausler, E. Griffiths, M. Ramezani, and P. Moghadam, “Towards long-term robotics in the wild,” arXiv preprint arXiv:2404.18477, 2024.
- https://arxiv.org/pdf/2404.18477 -- Towards long-term robotics in the wild


Actually a very few datasets are available:
- About Datasets, hosts for Wild Scenes and Wild Places.
- https://paperswithcode.com/dataset/freiburg-forest
-- Best on Frieburg: https://github.com/PramuPerera/In2I
