Here’s the **30/60/90-day plan**. Do the accessibility and content-safety work first; it protects users and strengthens credibility. Then make the platform easier to maintain and scale. [1]

## First 30 Days

**Goal: Fix the visible and high-risk gaps without rebuilding the site.**

- Run a full accessibility pass: keyboard-only navigation, visible focus states, semantic headings, ARIA labels where needed, form labels/errors, and color-contrast testing for amber-on-dark text. [1]
- Add loading states to every Markdown-driven session: skeleton loaders or a clear “Loading session…” indicator, plus readable error states when a file fails. [1]
- Improve form feedback: show clear success confirmation after submission and field-specific error messages when validation fails. [1]
- Test the curriculum on real phones—not just browser resizing—and simplify the mobile table of contents if it blocks reading or requires too many taps. [1]
- Create a content inventory: every session, Markdown file, internal link, image, script, protocol, facilitator asset, and its owning location.

**Deliverables**
- Accessibility issue list ranked Critical / High / Normal.
- Mobile usability notes with screenshots or recorded test cases.
- Markdown and internal-link inventory.
- Basic loading and form-feedback components live.

## Days 31–60

**Goal: Make the curriculum content deeper, navigable, and more durable.**

- Build dedicated core-concept pages for the **Survival Map** and **Trajectory Engine**, since the assessment identifies those concepts as too briefly treated in standalone Markdown. [1]
- Add consistent navigation at the end of every lesson: Previous Session, Next Session, Return to Part, and related concepts.
- Establish a standard Markdown template: learning objective, safety/boundary note where relevant, core teaching sections, case study, reflection, resources, and next action.
- Add automated internal-link checking in GitHub Actions so a renamed file does not quietly break the curriculum.
- Establish a content review protocol: version numbers, change log, reviewer, review date, and approval state for safety-critical material.

**Deliverables**
- Two core-concept explainer pages.
- Curriculum Markdown template and authoring guide.
- Automated broken-link report in GitHub.
- Versioned safety and facilitator-document review process.

## Days 61–90

**Goal: Shift from a strong static site into a platform that can grow without becoming a maintenance mess.**

- Introduce a light build pipeline—**Vite** is the clean choice for the current HTML, Tailwind CSS, and vanilla JavaScript setup—to bundle and minify assets, organize JavaScript as modules, and optimize production files. The assessment specifically identifies the lack of a build process as the key technical scalability gap. [1]
- Add a caching strategy for curriculum files. At minimum, configure cache headers; ideally add a service worker so recently viewed sessions remain available and unnecessary Markdown downloads are reduced. [1]
- Decide whether important curriculum pages should be pre-rendered or built into static HTML for stronger indexing, initial-load behavior, and failure resilience than pure client-side Markdown rendering. [1]
- Set performance baselines: mobile Lighthouse scores, largest-contentful paint, total JavaScript/CSS weight, broken links, and accessibility score.
- Create a release checklist requiring a content check, link check, mobile test, accessibility scan, and facilitator/safety review before publishing.

**Deliverables**
- Vite-based production build and deployment workflow.
- Cached curriculum delivery.
- Performance and accessibility baseline report.
- Written release checklist tied to GitHub deployment.

## Priority Order

| Rank | Work | Why it comes first |
|---|---|---|
| 1 | Accessibility and contrast audit | A trauma-informed curriculum cannot leave users unable to read, navigate, or use it independently. [1] |
| 2 | Loading, error, and form feedback | Users need to know whether the system is working, especially on slow connections or during contact/safety-related actions. [1] |
| 3 | Content ownership and link control | Markdown is efficient, but unmanaged links and duplicated content become a maintenance failure point. [1] |
| 4 | Deeper concept pages | The curriculum’s strongest framework should not be underexplained at the points learners need it most. [1] |
| 5 | Build process and caching | This is the scalable technical foundation, but it should not delay immediate usability and access fixes. [1] |

