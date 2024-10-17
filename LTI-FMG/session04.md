# PRD: LTI Implementation for Applicant Tracking System (ATS)

## User Stories

### User Story 1: Integration of LTI with LMS for Job Candidate Assessments
- **As a** recruiter
- **I want** to integrate an LMS (Learning Management System) with the ATS using LTI standards
- **So that** I can assign job candidates assessments or training tasks directly within the ATS and track their results seamlessly.

#### Acceptance Criteria:
1. The ATS should allow recruiters to assign assessments from an integrated LMS.
2. The results of the assessment should automatically sync and appear in the ATS under the candidate's profile.
3. Single sign-on (SSO) should be enabled for candidates to move from ATS to LMS without additional logins.
4. The ATS should provide notifications to recruiters once a candidate completes the assigned task.

### User Story 2: Candidate Progress Tracking with LTI-Integrated Tools
- **As a** hiring manager
- **I want** to track candidate progress across multiple LTI-integrated learning platforms
- **So that** I can monitor how candidates perform on different assessments or training sessions as part of the selection process.

#### Acceptance Criteria:
1. ATS should display progress reports from LTI-integrated learning platforms.
2. Each report should include metrics like completion rate, scores, and feedback, if applicable.
3. Progress tracking should be visible in real-time and update automatically without manual input.

### User Story 3: Automated Job Candidate Data Exchange Between ATS and LMS
- **As a** system administrator
- **I want** the ATS to automatically exchange data with the LMS via LTI, including job candidate profile updates
- **So that** data between both systems remains synchronized without manual intervention.

#### Acceptance Criteria:
1. The system should automatically send candidate profile data from ATS to LMS when updated.
2. Data exchanges should be secure, utilizing LTI 1.3 or higher.
3. All updates and synchronization logs should be available for auditing by system administrators.

---

## Product Backlog

### Methodology for Prioritization: **MoSCoW (Must have, Should have, Could have, Won't have)**
The backlog items are prioritized using the **MoSCoW** method, which is a widely used prioritization technique in Agile. We prioritize based on the business value and necessity for the initial release of LTI integration.

### Backlog Items (User Stories):
1. **Must have**: Integration of LTI with LMS for Job Candidate Assessments.
   - Critical for enabling the core functionality of ATS with LTI standards.
2. **Should have**: Candidate Progress Tracking with LTI-Integrated Tools.
   - Enhances recruiter experience and is key to tracking candidate performance during the hiring process.
3. **Could have**: Automated Job Candidate Data Exchange Between ATS and LMS.
   - Provides automated updates, reducing manual work but can be deferred to later releases.

### Prompts Used for Product Backlog Generation

#### Prompt 1:
*"Based on the user stories above, generate a product backlog using the MoSCoW prioritization method, placing the most critical features first."*

#### Prompt 2:
*"Generate a product backlog with prioritized user stories for the LTI integration into ATS using the MoSCoW prioritization method, ensuring essential features are labeled as ‘Must have.’"*

#### Prompt 3:
*"Create a detailed product backlog for LTI integration into ATS, focusing on the critical path using MoSCoW, and include user stories with priority explanations."*

#### Best Prompt: **Prompt 2**
This prompt yielded the most effective results as it clearly focused on prioritization using the MoSCoW method. It balanced prioritizing the most necessary features for initial implementation, while also listing less critical features for future releases.

---

## Work Tickets for Selected User Story

### Selected User Story: Integration of LTI with LMS for Job Candidate Assessments

#### Work Ticket 1: Setup LTI Authentication and Authorization
- **Description**: Implement LTI authentication using OAuth 2.0 standards to allow candidates to seamlessly authenticate between the ATS and the LMS.
- **Technical Details**:
  1. Configure OAuth 2.0 flow between ATS and LMS platforms.
  2. Implement token-based authentication for secure data exchange.
  3. Ensure that single sign-on (SSO) works across the ATS and LMS.

#### Work Ticket 2: Sync Candidate Data between ATS and LMS
- **Description**: Implement automatic syncing of candidate profiles and assessment results from the LMS back to the ATS.
- **Technical Details**:
  1. Use LTI launch requests to exchange candidate data.
  2. Ensure that assessment completion and results are automatically updated in the ATS.
  3. Develop error handling for any sync failures.

#### Work Ticket 3: User Interface (UI) for Assigning LMS Assessments in ATS
- **Description**: Create a user-friendly interface for recruiters to assign assessments to candidates via the ATS.
- **Technical Details**:
  1. Design a dashboard for recruiters to select assessments from the LMS.
  2. Enable filters to search for specific assessments.
  3. Integrate a drag-and-drop feature to assign assessments to candidates.

#### Work Ticket 4: Notifications for Recruiters on Candidate Task Completion
- **Description**: Develop a notification system to alert recruiters once a candidate completes an assessment on the LMS.
- **Technical Details**:
  1. Implement a notification service within the ATS.
  2. Trigger notifications based on the completion status received from the LMS via LTI.
  3. Ensure notifications are visible in the recruiter’s dashboard and via email.

---

# Effort Estimation for LTI Implementation

## Assumptions
- **Story Points (SP)** are estimated based on the complexity and expected duration of each task.
- We use the **Fibonacci sequence** for story point estimation (1, 2, 3, 5, 8, 13, etc.).
- Effort estimation is based on a small Scrum team with experience in LTI and ATS integrations.

## Work Tickets Effort Estimation

| **Work Ticket**                                             | **Description**                                        | **Story Points (SP)** | **Effort (Days)** | **Priority** |
|-------------------------------------------------------------|--------------------------------------------------------|-----------------------|-------------------|--------------|
| **WT 1: Setup LTI Authentication and Authorization**        | Configure OAuth 2.0 and SSO between ATS and LMS        | 8                     | 5                 | Must Have    |
| **WT 2: Sync Candidate Data between ATS and LMS**           | Implement automatic syncing of candidate profiles      | 8                     | 5                 | Must Have    |
| **WT 3: User Interface for Assigning LMS Assessments**      | Design and implement the UI for assigning assessments  | 13                    | 8                 | Must Have    |
| **WT 4: Notifications for Recruiters on Task Completion**   | Develop a notification system for recruiters           | 5                     | 3                 | Should Have  |

## Total Estimated Effort
- **Total Story Points**: 34 SP
- **Total Effort**: 21 Days

---

## Effort Estimation Breakdown

| **Category**           | **Total Story Points (SP)** | **Total Effort (Days)** |
|------------------------|----------------------------|-------------------------|
| Must Have (Critical)    | 29 SP                      | 18 Days                 |
| Should Have (Important) | 5 SP                       | 3 Days                  |

---

## Conclusion
Based on the estimated effort, the LTI integration for the ATS would require approximately **21 days** of work for a small Scrum team. The **must-have** features take the majority of the effort, totaling 18 days, while the **should-have** notification feature can be completed in an additional 3 days.
