import json
from bs4 import BeautifulSoup

# HTML content of the webpage
html = '''
<body dir="ltr" class="render-mode-BIGPIPE nav-v2 ember-application icons-loaded boot-complete" data-t-link-to-event-attached="true">
  

  
    <!-- HUED-11420 -->
    <div id="artdeco-toasts__wormhole" role="region">    <section id="artdeco-toasts" class="artdeco-toasts" aria-label="Toast message">
      <header class="artdeco-toasts__header">
        <h2 class="artdeco-toasts__title">
          0 notifications total
        </h2>
      </header>

<!---->
      <div class="artdeco-toasts_toasts">
<!---->      </div>
    </section>
</div>
    <!-- EMBER_CLI_FASTBOOT_BODY -->
<div id="app-boot-bg-loader" class="app-boot-bg-skeleton">
  <div class="top-bar"></div>
  <div class="content">
    <div class="initial-load-animation fade-load">
      <div class="linkedin-image display-flex justify-center">
        <svg xmlns="http://www.w3.org/2000/svg" class="loader__linkedin-logo" width="190" height="48" viewBox="0 0 190 48">
          <g>
            <g>
              <path d="M58,27.22V41H51V28.88c0-3.7-2.07-5.24-4-5.24a5,5,0,0,0-5.14,4.85,4.34,4.34,0,0,0,0,.51V41H35V18h6.6v3.25h.09c.69-1.41,3.64-3.75,7.66-3.75S58,20.22,58,27.22ZM24,41h7V18H24ZM27.5,6.45a4.05,4.05,0,1,0,4.1,4.05,4,4,0,0,0-4-4ZM190,3.5v41a3.5,3.5,0,0,1-3.5,3.5h-41a3.5,3.5,0,0,1-3.5-3.5V3.5A3.5,3.5,0,0,1,145.5,0h41A3.5,3.5,0,0,1,190,3.5ZM156,18h-7V41h7Zm.6-7.5a4.1,4.1,0,1,0-4.15,4.05h.05a4,4,0,0,0,4.1-3.9ZM183,27.22c0-7-4.63-9.72-8.65-9.72s-7,2.34-7.66,3.75h-.09V18H160V41h7V29c0-3.69,2.51-5.33,4.95-5.33,2,0,4.05,1.54,4.05,5.24V41h7ZM8,7H0V41H21V34H8ZM108,29.77v2H91a1.33,1.33,0,0,0,.11.43c.58,1.93,2.67,3.56,5.75,3.56A6.3,6.3,0,0,0,102,33.52l5.1,3.18a12.72,12.72,0,0,1-10.45,4.8C89.94,41.5,84,37.42,84,29.59S90,17.5,96.44,17.5,108,21.81,108,29.77ZM101,27c0-2.4-1.56-4.38-4.75-4.38-3,0-5.09,2-5.25,4.38ZM85.26,18H76.68l-7.54,9.37H69V7H62V41h7V30h.14l7.72,11h8.77L76.2,28.43ZM128,7h7V41h-6.6V38h-.09c-.88,1.52-3.24,3.49-7.4,3.49-5,0-10.91-3.63-10.91-12,0-7.53,5.1-11.95,10.82-11.95a9.55,9.55,0,0,1,7.09,3H128Zm.3,22.49a5.74,5.74,0,0,0-5.59-5.89h-.15A5.54,5.54,0,0,0,116.89,29c0,.15,0,.29,0,.44a5.61,5.61,0,0,0,5.26,5.94h.4A5.83,5.83,0,0,0,128.3,29.49Z" fill="currentColor"></path>
            </g>
          </g>
        </svg>
      </div>
      <div class="loading-bar">
        <div class="blue-bar"></div>
      </div>
    </div>
  </div>
</div>

    <script src="https://static.licdn.com/sc/h/9vghoawmkb5fvzav7oabel24l" data-fastboot-src="/assets/vendor-static.js" crossorigin=""></script>
    <script src="https://static.licdn.com/sc/h/3e6eewucbw1gbczk0tyi72jc0" data-fastboot-src="/assets/vendor.js" crossorigin=""></script>
    <!-- graphql-script-injection -->
    <script src="https://static.licdn.com/sc/h/a8i9w57wqoyi8fjxs9ulzk14e" data-fastboot-src="/assets/pdsc/register-metadata.js" crossorigin=""></script>
    <script src="https://static.licdn.com/sc/h/bkqsxwg84pfpt8s93ohkp8aap" data-fastboot-src="/assets/chunk.762.25c5d5d495a61e11176c.js" crossorigin=""></script>
<script src="https://static.licdn.com/sc/h/5a5yi3s31vu88brgkpjl38lt4" data-fastboot-src="/assets/chunk.143.6e6f6a15c29bc0b08759.js" crossorigin=""></script>
    <script data-embroider-ignore="" src="https://static.licdn.com/sc/h/4wh3anx58481m7t9qhuq6mulf" data-fastboot-src="/assets/i18n/support_en_US.js" crossorigin=""></script>
    <script src="https://static.licdn.com/sc/h/bxos6848mgy9f41dd37a8926e"></script><script src="https://static.licdn.com/sc/h/ewbyz9b62j144dxymday3brfs"></script><script src="https://static.licdn.com/sc/h/8tmwnm6o726keyh5rwewqriz"></script><script src="https://static.licdn.com/sc/h/1t6yb4fny1c4w3hllcuzdtdow"></script><script src="https://static.licdn.com/sc/h/aeyq66kqlm8crpr60rcur04fh"></script>
    <script src="https://static.licdn.com/sc/h/cvc7fiiwkg9puk0wrzpdysatn" data-fastboot-src="/assets/voyager-web.js" crossorigin=""></script>
    <div id="artdeco-modal-outlet"></div>

<code style="display: none" id="bpr-guid-104256">
  {"data":{"entityUrn":"urn:li:collectionResponse:4HlijJjSiEXmgxSNTaZbyKnZ88db1eTefgOnimBx6wM=","elements":[],"paging":{"count":10,"start":0,"links":[]},"$type":"com.linkedin.restli.common.CollectionResponse"},"included":[]}
</code>
<code style="display: none" id="datalet-bpr-guid-104256">
  {"request":"/voyager/api/voyagerSegmentsDashChameleonConfig","status":200,"body":"bpr-guid-104256","method":"GET","headers":{"x-li-uuid":"AAX9pWM/tcB+TnflXcw30Q\u003D\u003D"}}
</code>
<img src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" style="display: none" class="datalet-bpr-guid-104256"><code style="display: none" id="bpr-guid-104258">
  {"data":{"plainId":793767623,"publicContactInfo":{"$type":"com.linkedin.voyager.identity.shared.PublicContactInfo"},"premiumSubscriber":false,"*miniProfile":"urn:li:fs_miniProfile:ACoAAC9P7scB1yv1hA-ZjtKBAxcuNQvmvu08uhI","$type":"com.linkedin.voyager.common.Me"},"included":[{"customPronoun":null,"memorialized":false,"lastName":"Al-Safi","dashEntityUrn":"urn:li:fsd_profile:ACoAAC9P7scB1yv1hA-ZjtKBAxcuNQvmvu08uhI","standardizedPronoun":null,"occupation":"Software Engineer | Computer Engineer | AI Enthusiast","objectUrn":"urn:li:member:793767623","backgroundImage":{"artifacts":[{"width":800,"fileIdentifyingUrlPathSegment":"200_800/0/1619145014133?e=1691625600&amp;v=beta&amp;t=WNJVHkD-IOqS7Cro0mPXbkkXcylhyc4XywGf7-ZVYRs","expiresAt":1691625600000,"height":200,"$type":"com.linkedin.common.VectorArtifact"},{"width":1400,"fileIdentifyingUrlPathSegment":"350_1400/0/1619145014133?e=1691625600&amp;v=beta&amp;t=CCLM2DPbxKAIxgLF76CdQ1Gp-FUJMQmjz1DQmsMOOfU","expiresAt":1691625600000,"height":350,"$type":"com.linkedin.common.VectorArtifact"}],"rootUrl":"https://media.licdn.com/dms/image/C4E16AQHpKX8W_8U4dQ/profile-displaybackgroundimage-shrink_","$type":"com.linkedin.common.VectorImage"},"picture":{"artifacts":[{"width":100,"fileIdentifyingUrlPathSegment":"100_100/0/1675373176223?e=1691625600&amp;v=beta&amp;t=-3k4RuOJvA8N9zuEKPE4wNyFxg7L6jKBLgCDUEe33ec","expiresAt":1691625600000,"height":100,"$type":"com.linkedin.common.VectorArtifact"},{"width":200,"fileIdentifyingUrlPathSegment":"200_200/0/1675373176223?e=1691625600&amp;v=beta&amp;t=_9o-z2z8w540NQAt4gMeniczzyyKkD0PQPcIiPgetgo","expiresAt":1691625600000,"height":200,"$type":"com.linkedin.common.VectorArtifact"},{"width":400,"fileIdentifyingUrlPathSegment":"400_400/0/1675373176223?e=1691625600&amp;v=beta&amp;t=OfegiYnmbSi2ez4L2Z9exoHtI1j77ximISKDtpMfBeM","expiresAt":1691625600000,"height":400,"$type":"com.linkedin.common.VectorArtifact"},{"width":800,"fileIdentifyingUrlPathSegment":"800_800/0/1675373176223?e=1691625600&amp;v=beta&amp;t=m1XIXW9S_uGc_fY4J_eZopCMpeJbO484Aha0oGVAeY8","expiresAt":1691625600000,"height":800,"$type":"com.linkedin.common.VectorArtifact"}],"rootUrl":"https://media.licdn.com/dms/image/D4E03AQGB3OP3rlsmtQ/profile-displayphoto-shrink_","$type":"com.linkedin.common.VectorImage"},"$type":"com.linkedin.voyager.identity.shared.MiniProfile","firstName":"Harith","entityUrn":"urn:li:fs_miniProfile:ACoAAC9P7scB1yv1hA-ZjtKBAxcuNQvmvu08uhI","publicIdentifier":"harith-al-safi","trackingId":"xLBNakSZQ+m7GqzzdX2BcA=="}]}
</code>
<code style="display: none" id="datalet-bpr-guid-104258">
  {"request":"/voyager/api/me","status":200,"body":"bpr-guid-104258","method":"GET","headers":{"x-li-uuid":"AAX9pWM/tcB+TnflXcw30Q\u003D\u003D"}}
</code>
<img src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" style="display: none" class="datalet-bpr-guid-104258"><code style="display: none" id="bpr-guid-104262">
  {"data":{"data":{"feedDashGlobalNavs":{"logo":{"controlName":"nav_inbug","logo":{"attributes":[{"scalingType":null,"detailData":{"profilePictureWithoutFrame":null,"profilePictureWithRingStatus":null,"companyLogo":null,"icon":"IC_APP_LINKEDIN_BUG_COLOR_24DP","systemImage":null,"nonEntityGroupLogo":null,"vectorImage":null,"nonEntityProfessionalEventLogo":null,"profilePicture":null,"imageUrl":null,"professionalEventLogo":null,"nonEntityCompanyLogo":null,"nonEntitySchoolLogo":null,"groupLogo":null,"schoolLogo":null,"ghostImage":null,"nonEntityProfilePicture":null},"tintColor":null,"$recipeTypes":["com.linkedin.e6506ba5f5cc1a9b5124781a3661a7db"],"tapTargets":[],"displayAspectRatio":null,"$type":"com.linkedin.voyager.dash.common.image.ImageAttribute"}],"actionTarget":"https://www.linkedin.com/feed/?doFeedRefresh=true&amp;nis=true","accessibilityTextAttributes":[],"totalCount":null,"accessibilityText":"LinkedIn","$recipeTypes":["com.linkedin.f89edd0cdc11632a12f86e550f2f5e46"],"$type":"com.linkedin.voyager.dash.common.image.ImageViewModel"},"$recipeTypes":["com.linkedin.4973670c8e07d9bf8572c4c7f8658e2b"],"hoverText":null,"$type":"com.linkedin.voyager.dash.feed.nav.BrandingLogo"},"$recipeTypes":["com.linkedin.eae2ed6e463973c8e0d55baecd814363"],"spotlight":{"navContent":{"*premiumUpsellSlotUrn":"urn:li:fsd_premiumUpsellSlot:NAV_SPOTLIGHT","navElement":null},"type":"PREMIUM_UPSELL","$recipeTypes":["com.linkedin.c7f876e8e9f8a631b2896f62a656ce64"],"$type":"com.linkedin.voyager.dash.feed.nav.NavItem"},"primaryItems":[{"appLauncher":null,"navItem":{"navContent":{"navElement":{"activeIcon":{"attributes":[{"scalingType":null,"detailData":{"profilePictureWithoutFrame":null,"profilePictureWithRingStatus":null,"companyLogo":null,"icon":"IC_NAV_SMALL_HOME_ACTIVE_24DP","systemImage":null,"nonEntityGroupLogo":null,"vectorImage":null,"nonEntityProfessionalEventLogo":null,"profilePicture":null,"imageUrl":null,"professionalEventLogo":null,"nonEntityCompanyLogo":null,"nonEntitySchoolLogo":null,"groupLogo":null,"schoolLogo":null,"ghostImage":null,"nonEntityProfilePicture":null},"tintColor":null,"$recipeTypes":["com.linkedin.e6506ba5f5cc1a9b5124781a3661a7db"],"tapTargets":[],"displayAspectRatio":null,"$type":"com.linkedin.voyager.dash.common.image.ImageAttribute"}],"actionTarget":null,"accessibilityTextAttributes":[],"totalCount":null,"accessibilityText":null,"$recipeTypes":["com.linkedin.f89edd0cdc11632a12f86e550f2f5e46"],"$type":"com.linkedin.voyager.dash.common.image.ImageViewModel"},"staticIcon":{"attributes":[{"scalingType":null,"detailData":{"profilePictureWithoutFrame":null,"profilePictureWithRingStatus":null,"companyLogo":null,"icon":"IC_NAV_SMALL_HOME_24DP","systemImage":null,"nonEntityGroupLogo":null,"vectorImage":null,"nonEntityProfessionalEventLogo":null,"profilePicture":null,"imageUrl":null,"professionalEventLogo":null,"nonEntityCompanyLogo":null,"nonEntitySchoolLogo":null,"groupLogo":null,"schoolLogo":null,"ghostImage":null,"nonEntityProfilePicture":null},"tintColor":null,"$recipeTypes":["com.linkedin.e6506ba5f5cc1a9b5124781a3661a7db"],"tapTargets":[],"displayAspectRatio":null,"$type":"com.linkedin.voyager.dash.common.image.ImageAttribute"}],"actionTarget":null,"accessibilityTextAttributes":[],"totalCount":null,"accessibilityText":null,"$recipeTypes":["com.linkedin.f89edd0cdc11632a12f86e550f2f5e46"],"$type":"com.linkedin.voyager.dash.common.image.ImageViewModel"},"hasCoachmark":false,"controlName":"nav_homepage","showIconBorder":false,"actionTarget":"https://www.linkedin.com/feed/?doFeedRefresh=true&amp;nis=true","text":"Home","$recipeTypes":["com.linkedin.b2c03744140a6cd6a2e693c32790988c"],"hasPaid":false,"$type":"com.linkedin.voyager.dash.feed.nav.NavElement"},"premiumUpsellSlotUrn":null},"type":"HOME","$recipeTypes":["com.linkedin.c7f876e8e9f8a631b2896f62a656ce64"],"$type":"com.linkedin.voyager.dash.feed.nav.NavItem"},"meMenu":null},{"appLauncher":null,"navItem":{"navContent":{"navElement":{"activeIcon":{"attributes":[{"scalingType":null,"detailData":{"profilePictureWithoutFrame":null,"profilePictureWithRingStatus":null,"companyLogo":null,"icon":"IC_NAV_SMALL_PEOPLE_ACTIVE_24DP","systemImage":null,"nonEntityGroupLogo":null,"vectorImage":null,"nonEntityProfessionalEventLogo":null,"profilePicture":null,"imageUrl":null,"professionalEventLogo":null,"nonEntityCompanyLogo":null,"nonEntitySchoolLogo":null,"groupLogo":null,"schoolLogo":null,"ghostImage":null,"nonEntityProfilePicture":null},"tintColor":null,"$recipeTypes":["com.linkedin.e6506ba5f5cc1a9b5124781a3661a7db"],"tapTargets":[],"displayAspectRatio":null,"$type":"com.linkedin.voyager.dash.common.image.ImageAttribute"}],"actionTarget":null,"accessibilityTextAttributes":[],"totalCount":null,"accessibilityText":null,"$recipeTypes":["com.linkedin.f89edd0cdc11632a12f86e550f2f5e46"],"$type":"com.linkedin.voyager.dash.common.image.ImageViewModel"},"staticIcon":{"attributes":[{"scalingType":null,"detailData":{"profilePictureWithoutFrame":null,"profilePictureWithRingStatus":null,"companyLogo":null,"icon":"IC_NAV_SMALL_PEOPLE_24DP","systemImage":null,"nonEntityGroupLogo":null,"vectorImage":null,"nonEntityProfessionalEventLogo":null,"profilePicture":null,"imageUrl":null,"professionalEventLogo":null,"nonEntityCompanyLogo":null,"nonEntitySchoolLogo":null,"groupLogo":null,"schoolLogo":null,"ghostImage":null,"nonEntityProfilePicture":null},"tintColor":null,"$recipeTypes":["com.linkedin.e6506ba5f5cc1a9b5124781a3661a7db"],"tapTargets":[],"displayAspectRatio":null,"$type":"com.linkedin.voyager.dash.common.image.ImageAttribute"}],"actionTarget":null,"accessibilityTextAttributes":[],"totalCount":null,"accessibilityText":null,"$recipeTypes":["com.linkedin.f89edd0cdc11632a12f86e550f2f5e46"],"$type":"com.linkedin.voyager.dash.common.image.ImageViewModel"},"hasCoachmark":false,"controlName":"nav_mynetwork","showIconBorder":false,"actionTarget":"https://www.linkedin.com/mynetwork/","text":"My Network","$recipeTypes":["com.linkedin.b2c03744140a6cd6a2e693c32790988c"],"hasPaid":false,"$type":"com.linkedin.voyager.dash.feed.nav.NavElement"},"premiumUpsellSlotUrn":null},"type":"MY_NETWORK","$recipeTypes":["com.linkedin.c7f876e8e9f8a631b2896f62a656ce64"],"$type":"com.linkedin.voyager.dash.feed.nav.NavItem"},"meMenu":null},{"appLauncher":null,"navItem":{"navContent":{"navElement":{"activeIcon":{"attributes":[{"scalingType":null,"detailData":{"profilePictureWithoutFrame":null,"profilePictureWithRingStatus":null,"companyLogo":null,"icon":"IC_NAV_SMALL_JOBS_ACTIVE_24DP","systemImage":null,"nonEntityGroupLogo":null,"vectorImage":null,"nonEntityProfessionalEventLogo":null,"profilePicture":null,"imageUrl":null,"professionalEventLogo":null,"nonEntityCompanyLogo":null,"nonEntitySchoolLogo":null,"groupLogo":null,"schoolLogo":null,"ghostImage":null,"nonEntityProfilePicture":null},"tintColor":null,"$recipeTypes":["com.linkedin.e6506ba5f5cc1a9b5124781a3661a7db"],"tapTargets":[],"displayAspectRatio":null,"$type":"com.linkedin.voyager.dash.common.image.ImageAttribute"}],"actionTarget":null,"accessibilityTextAttributes":[],"totalCount":null,"accessibilityText":null,"$recipeTypes":["com.linkedin.f89edd0cdc11632a12f86e550f2f5e46"],"$type":"com.linkedin.voyager.dash.common.image.ImageViewModel"},"staticIcon":{"attributes":[{"scalingType":null,"detailData":{"profilePictureWithoutFrame":null,"profilePictureWithRingStatus":null,"companyLogo":null,"icon":"IC_NAV_SMALL_JOBS_24DP","systemImage":null,"nonEntityGroupLogo":null,"vectorImage":null,"nonEntityProfessionalEventLogo":null,"profilePicture":null,"imageUrl":null,"professionalEventLogo":null,"nonEntityCompanyLogo":null,"nonEntitySchoolLogo":null,"groupLogo":null,"schoolLogo":null,"ghostImage":null,"nonEntityProfilePicture":null},"tintColor":null,"$recipeTypes":["com.linkedin.e6506ba5f5cc1a9b5124781a3661a7db"],"tapTargets":[],"displayAspectRatio":null,"$type":"com.linkedin.voyager.dash.common.image.ImageAttribute"}],"actionTarget":null,"accessibilityTextAttributes":[],"totalCount":null,"accessibilityText":null,"$recipeTypes":["com.linkedin.f89edd0cdc11632a12f86e550f2f5e46"],"$type":"com.linkedin.voyager.dash.common.image.ImageViewModel"},"hasCoachmark":false,"controlName":"nav_jobs","showIconBorder":false,"actionTarget":"https://www.linkedin.com/jobs/","text":"Jobs","$recipeTypes":["com.linkedin.b2c03744140a6cd6a2e693c32790988c"],"hasPaid":false,"$type":"com.linkedin.voyager.dash.feed.nav.NavElement"},"premiumUpsellSlotUrn":null},"type":"JOBS","$recipeTypes":["com.linkedin.c7f876e8e9f8a631b2896f62a656ce64"],"$type":"com.linkedin.voyager.dash.feed.nav.NavItem"},"meMenu":null},{"appLauncher":null,"navItem":{"navContent":{"navElement":{"activeIcon":{"attributes":[{"scalingType":null,"detailData":{"profilePictureWithoutFrame":null,"profilePictureWithRingStatus":null,"companyLogo":null,"icon":"IC_NAV_SMALL_MESSAGING_ACTIVE_24DP","systemImage":null,"nonEntityGroupLogo":null,"vectorImage":null,"nonEntityProfessionalEventLogo":null,"profilePicture":null,"imageUrl":null,"professionalEventLogo":null,"nonEntityCompanyLogo":null,"nonEntitySchoolLogo":null,"groupLogo":null,"schoolLogo":null,"ghostImage":null,"nonEntityProfilePicture":null},"tintColor":null,"$recipeTypes":["com.linkedin.e6506ba5f5cc1a9b5124781a3661a7db"],"tapTargets":[],"displayAspectRatio":null,"$type":"com.linkedin.voyager.dash.common.image.ImageAttribute"}],"actionTarget":null,"accessibilityTextAttributes":[],"totalCount":null,"accessibilityText":null,"$recipeTypes":["com.linkedin.f89edd0cdc11632a12f86e550f2f5e46"],"$type":"com.linkedin.voyager.dash.common.image.ImageViewModel"},"staticIcon":{"attributes":[{"scalingType":null,"detailData":{"profilePictureWithoutFrame":null,"profilePictureWithRingStatus":null,"companyLogo":null,"icon":"IC_NAV_SMALL_MESSAGING_24DP","systemImage":null,"nonEntityGroupLogo":null,"vectorImage":null,"nonEntityProfessionalEventLogo":null,"profilePicture":null,"imageUrl":null,"professionalEventLogo":null,"nonEntityCompanyLogo":null,"nonEntitySchoolLogo":null,"groupLogo":null,"schoolLogo":null,"ghostImage":null,"nonEntityProfilePicture":null},"tintColor":null,"$recipeTypes":["com.linkedin.e6506ba5f5cc1a9b5124781a3661a7db"],"tapTargets":[],"displayAspectRatio":null,"$type":"com.linkedin.voyager.dash.common.image.ImageAttribute"}],"actionTarget":null,"accessibilityTextAttributes":[],"totalCount":null,"accessibilityText":null,"$recipeTypes":["com.linkedin.f89edd0cdc11632a12f86e550f2f5e46"],"$type":"com.linkedin.voyager.dash.common.image.ImageViewModel"},"hasCoachmark":false,"controlName":"nav_messaging","showIconBorder":false,"actionTarget":"https://www.linkedin.com/messaging/","text":"Messaging","$recipeTypes":["com.linkedin.b2c03744140a6cd6a2e693c32790988c"],"hasPaid":false,"$type":"com.linkedin.voyager.dash.feed.nav.NavElement"},"premiumUpsellSlotUrn":null},"type":"MESSAGING","$recipeTypes":["com.linkedin.c7f876e8e9f8a631b2896f62a656ce64"],"$type":"com.linkedin.voyager.dash.feed.nav.NavItem"},"meMenu":null},{"appLauncher":null,"navItem":{"navContent":{"navElement":{"activeIcon":{"attributes":[{"scalingType":null,"detailData":{"profilePictureWithoutFrame":null,"profilePictureWithRingStatus":null,"companyLogo":null,"icon":"IC_NAV_SMALL_NOTIFICATIONS_ACTIVE_24DP","systemImage":null,"nonEntityGroupLogo":null,"vectorImage":null,"nonEntityProfessionalEventLogo":null,"profilePicture":null,"imageUrl":null,"professionalEventLogo":null,"nonEntityCompanyLogo":null,"nonEntitySchoolLogo":null,"groupLogo":null,"schoolLogo":null,"ghostImage":null,"nonEntityProfilePicture":null},"tintColor":null,"$recipeTypes":["com.linkedin.e6506ba5f5cc1a9b5124781a3661a7db"],"tapTargets":[],"displayAspectRatio":null,"$type":"com.linkedin.voyager.dash.common.image.ImageAttribute"}],"actionTarget":null,"accessibilityTextAttributes":[],"totalCount":null,"accessibilityText":null,"$recipeTypes":["com.linkedin.f89edd0cdc11632a12f86e550f2f5e46"],"$type":"com.linkedin.voyager.dash.common.image.ImageViewModel"},"staticIcon":{"attributes":[{"scalingType":null,"detailData":{"profilePictureWithoutFrame":null,"profilePictureWithRingStatus":null,"companyLogo":null,"icon":"IC_NAV_SMALL_NOTIFICATIONS_24DP","systemImage":null,"nonEntityGroupLogo":null,"vectorImage":null,"nonEntityProfessionalEventLogo":null,"profilePicture":null,"imageUrl":null,"professionalEventLogo":null,"nonEntityCompanyLogo":null,"nonEntitySchoolLogo":null,"groupLogo":null,"schoolLogo":null,"ghostImage":null,"nonEntityProfilePicture":null},"tintColor":null,"$recipeTypes":["com.linkedin.e6506ba5f5cc1a9b5124781a3661a7db"],"tapTargets":[],"displayAspectRatio":null,"$type":"com.linkedin.voyager.dash.common.image.ImageAttribute"}],"actionTarget":null,"accessibilityTextAttributes":[],"totalCount":null,"accessibilityText":null,"$recipeTypes":["com.linkedin.f89edd0cdc11632a12f86e550f2f5e46"],"$type":"com.linkedin.voyager.dash.common.image.ImageViewModel"},"hasCoachmark":false,"controlName":"nav_notifications","showIconBorder":false,"actionTarget":"https://www.linkedin.com/notifications/","text":"Notifications","$recipeTypes":["com.linkedin.b2c03744140a6cd6a2e693c32790988c"],"hasPaid":false,"$type":"com.linkedin.voyager.dash.feed.nav.NavElement"},"premiumUpsellSlotUrn":null},"type":"NOTIFICATIONS","$recipeTypes":["com.linkedin.c7f876e8e9f8a631b2896f62a656ce64"],"$type":"com.linkedin.voyager.dash.feed.nav.NavItem"},"meMenu":null},{"appLauncher":null,"meMenu":{"viewProfileText":"View Profile","*profile":"urn:li:fsd_profile:ACoAAC9P7scB1yv1hA-ZjtKBAxcuNQvmvu08uhI","meGroups":[{"meItems":[{"*premiumUpsellSlotUrn":"urn:li:fsd_premiumUpsellSlot:NAV_ME","meItem":null},{"meItem":{"controlName":"nav_settings_account_manage_account","actionTarget":"https://www.linkedin.com/mypreferences/d/","text":{"textDirection":"USER_LOCALE","text":"Settings &amp; Privacy","attributesV2":[],"accessibilityTextAttributesV2":[],"accessibilityText":null,"$recipeTypes":["com.linkedin.566376561ef86249fc89f5596eaf6fe1"],"$type":"com.linkedin.voyager.dash.common.text.TextViewModel"},"quickHelp":false,"$recipeTypes":["com.linkedin.fb4511fb6c2df4a805ef662367e15026"],"$type":"com.linkedin.voyager.dash.feed.nav.MeItem"},"premiumUpsellSlotUrn":null},{"meItem":{"controlName":"nav_settings_account_quick_help","actionTarget":"https://www.linkedin.com/help/linkedin/","text":{"textDirection":"USER_LOCALE","text":"Help","attributesV2":[],"accessibilityTextAttributesV2":[],"accessibilityText":null,"$recipeTypes":["com.linkedin.566376561ef86249fc89f5596eaf6fe1"],"$type":"com.linkedin.voyager.dash.common.text.TextViewModel"},"quickHelp":true,"$recipeTypes":["com.linkedin.fb4511fb6c2df4a805ef662367e15026"],"$type":"com.linkedin.voyager.dash.feed.nav.MeItem"},"premiumUpsellSlotUrn":null},{"meItem":{"controlName":"nav_settings_account_language","actionTarget":"https://www.linkedin.com/mypreferences/d/language/","text":{"textDirection":"USER_LOCALE","text":"Language","attributesV2":[],"accessibilityTextAttributesV2":[],"accessibilityText":null,"$recipeTypes":["com.linkedin.566376561ef86249fc89f5596eaf6fe1"],"$type":"com.linkedin.voyager.dash.common.text.TextViewModel"},"quickHelp":false,"$recipeTypes":["com.linkedin.fb4511fb6c2df4a805ef662367e15026"],"$type":"com.linkedin.voyager.dash.feed.nav.MeItem"},"premiumUpsellSlotUrn":null}],"title":"Account","$recipeTypes":["com.linkedin.bb35e914e880d9f9ad79d52bf644c44c"],"$type":"com.linkedin.voyager.dash.feed.nav.MeGroup"},{"meItems":[{"meItem":{"controlName":"recent_activity_nav_all","actionTarget":"https://www.linkedin.com/in/harith-al-safi/recent-activity/","text":{"textDirection":"USER_LOCALE","text":"Posts &amp; Activity","attributesV2":[],"accessibilityTextAttributesV2":[],"accessibilityText":null,"$recipeTypes":["com.linkedin.566376561ef86249fc89f5596eaf6fe1"],"$type":"com.linkedin.voyager.dash.common.text.TextViewModel"},"quickHelp":false,"$recipeTypes":["com.linkedin.fb4511fb6c2df4a805ef662367e15026"],"$type":"com.linkedin.voyager.dash.feed.nav.MeItem"},"premiumUpsellSlotUrn":null},{"meItem":{"controlName":"nav_settings_manage_job_posting_account","actionTarget":"https://www.linkedin.com/talent/job-management-redirect?trk=nav_app_launcher_manage_job_post_nept","text":{"textDirection":"USER_LOCALE","text":"Job Posting Account","attributesV2":[],"accessibilityTextAttributesV2":[],"accessibilityText":null,"$recipeTypes":["com.linkedin.566376561ef86249fc89f5596eaf6fe1"],"$type":"com.linkedin.voyager.dash.common.text.TextViewModel"},"quickHelp":false,"$recipeTypes":["com.linkedin.fb4511fb6c2df4a805ef662367e15026"],"$type":"com.linkedin.voyager.dash.feed.nav.MeItem"},"premiumUpsellSlotUrn":null}],"title":"Manage","$recipeTypes":["com.linkedin.bb35e914e880d9f9ad79d52bf644c44c"],"$type":"com.linkedin.voyager.dash.feed.nav.MeGroup"}],"controlName":"nav_settings","text":"Me","$recipeTypes":["com.linkedin.73113dd58d976ff22a5e4aa2ca35d21d"],"$type":"com.linkedin.voyager.dash.feed.nav.MeMenu"},"navItem":null},{"appLauncher":{"showDivider":true,"productItems":[{"navContent":{"navElement":{"staticIcon":{"attributes":[{"scalingType":null,"detailData":{"profilePictureWithoutFrame":null,"profilePictureWithRingStatus":null,"companyLogo":null,"icon":"IC_APP_LEARNING_24DP","systemImage":null,"nonEntityGroupLogo":null,"vectorImage":null,"nonEntityProfessionalEventLogo":null,"profilePicture":null,"imageUrl":null,"professionalEventLogo":null,"nonEntityCompanyLogo":null,"nonEntitySchoolLogo":null,"groupLogo":null,"schoolLogo":null,"ghostImage":null,"nonEntityProfilePicture":null},"tintColor":null,"$recipeTypes":["com.linkedin.e6506ba5f5cc1a9b5124781a3661a7db"],"tapTargets":[],"displayAspectRatio":null,"$type":"com.linkedin.voyager.dash.common.image.ImageAttribute"}],"actionTarget":null,"accessibilityTextAttributes":[],"totalCount":null,"accessibilityText":null,"$recipeTypes":["com.linkedin.f89edd0cdc11632a12f86e550f2f5e46"],"$type":"com.linkedin.voyager.dash.common.image.ImageViewModel"},"activeIcon":null,"hasCoachmark":false,"controlName":"nav_launcher_learning","showIconBorder":true,"actionTarget":"https://www.linkedin.com/learning/?trk=nav_neptune_learning","text":"Learning","$recipeTypes":["com.linkedin.b2c03744140a6cd6a2e693c32790988c"],"hasPaid":true,"$type":"com.linkedin.voyager.dash.feed.nav.NavElement"},"premiumUpsellSlotUrn":null},"type":"LEARNING","$recipeTypes":["com.linkedin.c7f876e8e9f8a631b2896f62a656ce64"],"$type":"com.linkedin.voyager.dash.feed.nav.NavItem"},{"navContent":{"navElement":{"staticIcon":{"attributes":[{"scalingType":null,"detailData":{"profilePictureWithoutFrame":null,"profilePictureWithRingStatus":null,"companyLogo":null,"icon":"IC_APP_TALENT_INSIGHTS_24DP","systemImage":null,"nonEntityGroupLogo":null,"vectorImage":null,"nonEntityProfessionalEventLogo":null,"profilePicture":null,"imageUrl":null,"professionalEventLogo":null,"nonEntityCompanyLogo":null,"nonEntitySchoolLogo":null,"groupLogo":null,"schoolLogo":null,"ghostImage":null,"nonEntityProfilePicture":null},"tintColor":null,"$recipeTypes":["com.linkedin.e6506ba5f5cc1a9b5124781a3661a7db"],"tapTargets":[],"displayAspectRatio":null,"$type":"com.linkedin.voyager.dash.common.image.ImageAttribute"}],"actionTarget":null,"accessibilityTextAttributes":[],"totalCount":null,"accessibilityText":null,"$recipeTypes":["com.linkedin.f89edd0cdc11632a12f86e550f2f5e46"],"$type":"com.linkedin.voyager.dash.common.image.ImageViewModel"},"activeIcon":null,"hasCoachmark":false,"controlName":"nav_launcher_insights","showIconBorder":true,"actionTarget":"https://www.linkedin.com/insights?trk=nav_app_launcher_insights_nept&amp;src=li-nav","text":"Insights","$recipeTypes":["com.linkedin.b2c03744140a6cd6a2e693c32790988c"],"hasPaid":false,"$type":"com.linkedin.voyager.dash.feed.nav.NavElement"},"premiumUpsellSlotUrn":null},"type":"INSIGHTS","$recipeTypes":["com.linkedin.c7f876e8e9f8a631b2896f62a656ce64"],"$type":"com.linkedin.voyager.dash.feed.nav.NavItem"},{"navContent":{"navElement":{"staticIcon":{"attributes":[{"scalingType":null,"detailData":{"profilePictureWithoutFrame":null,"profilePictureWithRingStatus":null,"companyLogo":null,"icon":"IC_APP_JOBS_POSTING_24DP","systemImage":null,"nonEntityGroupLogo":null,"vectorImage":null,"nonEntityProfessionalEventLogo":null,"profilePicture":null,"imageUrl":null,"professionalEventLogo":null,"nonEntityCompanyLogo":null,"nonEntitySchoolLogo":null,"groupLogo":null,"schoolLogo":null,"ghostImage":null,"nonEntityProfilePicture":null},"tintColor":null,"$recipeTypes":["com.linkedin.e6506ba5f5cc1a9b5124781a3661a7db"],"tapTargets":[],"displayAspectRatio":null,"$type":"com.linkedin.voyager.dash.common.image.ImageAttribute"}],"actionTarget":null,"accessibilityTextAttributes":[],"totalCount":null,"accessibilityText":null,"$recipeTypes":["com.linkedin.f89edd0cdc11632a12f86e550f2f5e46"],"$type":"com.linkedin.voyager.dash.common.image.ImageViewModel"},"activeIcon":null,"hasCoachmark":false,"controlName":"nav_launcher_job_postings","showIconBorder":true,"actionTarget":"https://www.linkedin.com/talent/job-posting-redirect?trk=nav_app_launcher_job_post_nept","text":"Post a job","$recipeTypes":["com.linkedin.b2c03744140a6cd6a2e693c32790988c"],"hasPaid":true,"$type":"com.linkedin.voyager.dash.feed.nav.NavElement"},"premiumUpsellSlotUrn":null},"type":"JOB_POSTINGS","$recipeTypes":["com.linkedin.c7f876e8e9f8a631b2896f62a656ce64"],"$type":"com.linkedin.voyager.dash.feed.nav.NavItem"},{"navContent":{"navElement":{"staticIcon":{"attributes":[{"scalingType":null,"detailData":{"profilePictureWithoutFrame":null,"profilePictureWithRingStatus":null,"companyLogo":null,"icon":"IC_APP_ADS_24DP","systemImage":null,"nonEntityGroupLogo":null,"vectorImage":null,"nonEntityProfessionalEventLogo":null,"profilePicture":null,"imageUrl":null,"professionalEventLogo":null,"nonEntityCompanyLogo":null,"nonEntitySchoolLogo":null,"groupLogo":null,"schoolLogo":null,"ghostImage":null,"nonEntityProfilePicture":null},"tintColor":null,"$recipeTypes":["com.linkedin.e6506ba5f5cc1a9b5124781a3661a7db"],"tapTargets":[],"displayAspectRatio":null,"$type":"com.linkedin.voyager.dash.common.image.ImageAttribute"}],"actionTarget":null,"accessibilityTextAttributes":[],"totalCount":null,"accessibilityText":null,"$recipeTypes":["com.linkedin.f89edd0cdc11632a12f86e550f2f5e46"],"$type":"com.linkedin.voyager.dash.common.image.ImageViewModel"},"activeIcon":null,"hasCoachmark":false,"controlName":"nav_launcher_ads","showIconBorder":true,"actionTarget":"https://www.linkedin.com/campaignmanager/accounts","text":"Advertise","$recipeTypes":["com.linkedin.b2c03744140a6cd6a2e693c32790988c"],"hasPaid":true,"$type":"com.linkedin.voyager.dash.feed.nav.NavElement"},"premiumUpsellSlotUrn":null},"type":"ADVERTISE","$recipeTypes":["com.linkedin.c7f876e8e9f8a631b2896f62a656ce64"],"$type":"com.linkedin.voyager.dash.feed.nav.NavItem"},{"navContent":{"navElement":{"staticIcon":{"attributes":[{"scalingType":null,"detailData":{"profilePictureWithoutFrame":null,"profilePictureWithRingStatus":null,"companyLogo":null,"icon":"IC_APP_SALES_NAVIGATOR_24DP","systemImage":null,"nonEntityGroupLogo":null,"vectorImage":null,"nonEntityProfessionalEventLogo":null,"profilePicture":null,"imageUrl":null,"professionalEventLogo":null,"nonEntityCompanyLogo":null,"nonEntitySchoolLogo":null,"groupLogo":null,"schoolLogo":null,"ghostImage":null,"nonEntityProfilePicture":null},"tintColor":null,"$recipeTypes":["com.linkedin.e6506ba5f5cc1a9b5124781a3661a7db"],"tapTargets":[],"displayAspectRatio":null,"$type":"com.linkedin.voyager.dash.common.image.ImageAttribute"}],"actionTarget":null,"accessibilityTextAttributes":[],"totalCount":null,"accessibilityText":null,"$recipeTypes":["com.linkedin.f89edd0cdc11632a12f86e550f2f5e46"],"$type":"com.linkedin.voyager.dash.common.image.ImageViewModel"},"activeIcon":null,"hasCoachmark":false,"controlName":"nav_launcher_find_leads","showIconBorder":true,"actionTarget":"https://www.linkedin.com/premium/products/?intentType=FIND_LEADS&amp;upsellOrderOrigin=premium_nav_more_products_panel&amp;utype=sales","text":"Find Leads","$recipeTypes":["com.linkedin.b2c03744140a6cd6a2e693c32790988c"],"hasPaid":false,"$type":"com.linkedin.voyager.dash.feed.nav.NavElement"},"premiumUpsellSlotUrn":null},"type":"FIND_LEADS","$recipeTypes":["com.linkedin.c7f876e8e9f8a631b2896f62a656ce64"],"$type":"com.linkedin.voyager.dash.feed.nav.NavItem"},{"navContent":{"navElement":{"staticIcon":{"attributes":[{"scalingType":null,"detailData":{"profilePictureWithoutFrame":null,"profilePictureWithRingStatus":null,"companyLogo":null,"icon":"IC_APP_GROUPS_24DP","systemImage":null,"nonEntityGroupLogo":null,"vectorImage":null,"nonEntityProfessionalEventLogo":null,"profilePicture":null,"imageUrl":null,"professionalEventLogo":null,"nonEntityCompanyLogo":null,"nonEntitySchoolLogo":null,"groupLogo":null,"schoolLogo":null,"ghostImage":null,"nonEntityProfilePicture":null},"tintColor":null,"$recipeTypes":["com.linkedin.e6506ba5f5cc1a9b5124781a3661a7db"],"tapTargets":[],"displayAspectRatio":null,"$type":"com.linkedin.voyager.dash.common.image.ImageAttribute"}],"actionTarget":null,"accessibilityTextAttributes":[],"totalCount":null,"accessibilityText":null,"$recipeTypes":["com.linkedin.f89edd0cdc11632a12f86e550f2f5e46"],"$type":"com.linkedin.voyager.dash.common.image.ImageViewModel"},"activeIcon":null,"hasCoachmark":false,"controlName":"nav_launcher_groups","showIconBorder":true,"actionTarget":"https://www.linkedin.com/groups","text":"Groups","$recipeTypes":["com.linkedin.b2c03744140a6cd6a2e693c32790988c"],"hasPaid":false,"$type":"com.linkedin.voyager.dash.feed.nav.NavElement"},"premiumUpsellSlotUrn":null},"type":"GROUPS","$recipeTypes":["com.linkedin.c7f876e8e9f8a631b2896f62a656ce64"],"$type":"com.linkedin.voyager.dash.feed.nav.NavItem"},{"navContent":{"navElement":{"staticIcon":{"attributes":[{"scalingType":null,"detailData":{"profilePictureWithoutFrame":null,"profilePictureWithRingStatus":null,"companyLogo":null,"icon":"IC_APP_PROFINDER_24DP","systemImage":null,"nonEntityGroupLogo":null,"vectorImage":null,"nonEntityProfessionalEventLogo":null,"profilePicture":null,"imageUrl":null,"professionalEventLogo":null,"nonEntityCompanyLogo":null,"nonEntitySchoolLogo":null,"groupLogo":null,"schoolLogo":null,"ghostImage":null,"nonEntityProfilePicture":null},"tintColor":null,"$recipeTypes":["com.linkedin.e6506ba5f5cc1a9b5124781a3661a7db"],"tapTargets":[],"displayAspectRatio":null,"$type":"com.linkedin.voyager.dash.common.image.ImageAttribute"}],"actionTarget":null,"accessibilityTextAttributes":[],"totalCount":null,"accessibilityText":null,"$recipeTypes":["com.linkedin.f89edd0cdc11632a12f86e550f2f5e46"],"$type":"com.linkedin.voyager.dash.common.image.ImageViewModel"},"activeIcon":null,"hasCoachmark":false,"controlName":"nav_launcher_services_marketplace","showIconBorder":true,"actionTarget":"https://www.linkedin.com/services?trk=d_flagship3_nav","text":"Services Marketplace","$recipeTypes":["com.linkedin.b2c03744140a6cd6a2e693c32790988c"],"hasPaid":false,"$type":"com.linkedin.voyager.dash.feed.nav.NavElement"},"premiumUpsellSlotUrn":null},"type":"PROFINDER","$recipeTypes":["com.linkedin.c7f876e8e9f8a631b2896f62a656ce64"],"$type":"com.linkedin.voyager.dash.feed.nav.NavItem"}],"businessServices":[{"businessServiceAction":{"controlName":"nav_business_talent_solutions","actionTarget":"https://business.linkedin.com/talent-solutions?trk=flagship_nav&amp;veh=li-header-dropdown-lts-control&amp;src=li-nav","title":{"textDirection":"USER_LOCALE","text":"Talent Solutions","attributesV2":[],"accessibilityTextAttributesV2":[],"accessibilityText":null,"$recipeTypes":["com.linkedin.566376561ef86249fc89f5596eaf6fe1"],"$type":"com.linkedin.voyager.dash.common.text.TextViewModel"},"$recipeTypes":["com.linkedin.188858304ae14097e59518d245c7cc85"],"$type":"com.linkedin.voyager.dash.feed.nav.BusinessServiceAction"},"description":"Find, attract and recruit talent","$recipeTypes":["com.linkedin.a94ff0919cddaa7056025e9491dc3794"],"$type":"com.linkedin.voyager.dash.feed.nav.BusinessService"},{"businessServiceAction":{"controlName":"nav_business_sales_solutions","actionTarget":"https://business.linkedin.com/sales-solutions?trk=flagship_nav&amp;veh=li-header-dropdown-lss-control&amp;src=li-nav","title":{"textDirection":"USER_LOCALE","text":"Sales Solutions","attributesV2":[],"accessibilityTextAttributesV2":[],"accessibilityText":null,"$recipeTypes":["com.linkedin.566376561ef86249fc89f5596eaf6fe1"],"$type":"com.linkedin.voyager.dash.common.text.TextViewModel"},"$recipeTypes":["com.linkedin.188858304ae14097e59518d245c7cc85"],"$type":"com.linkedin.voyager.dash.feed.nav.BusinessServiceAction"},"description":"Unlock sales opportunities","$recipeTypes":["com.linkedin.a94ff0919cddaa7056025e9491dc3794"],"$type":"com.linkedin.voyager.dash.feed.nav.BusinessService"},{"businessServiceAction":{"controlName":"nav_business_post_a_job","actionTarget":"https://www.linkedin.com/talent/job-posting-redirect?trk=nav_biz_serv_job_post_nept","title":{"textDirection":"USER_LOCALE","text":"Post a job for free","attributesV2":[],"accessibilityTextAttributesV2":[],"accessibilityText":null,"$recipeTypes":["com.linkedin.566376561ef86249fc89f5596eaf6fe1"],"$type":"com.linkedin.voyager.dash.common.text.TextViewModel"},"$recipeTypes":["com.linkedin.188858304ae14097e59518d245c7cc85"],"$type":"com.linkedin.voyager.dash.feed.nav.BusinessServiceAction"},"description":"Get your job in front of quality candidates","$recipeTypes":["com.linkedin.a94ff0919cddaa7056025e9491dc3794"],"$type":"com.linkedin.voyager.dash.feed.nav.BusinessService"},{"businessServiceAction":{"controlName":"nav_business_advertise","actionTarget":"https://business.linkedin.com/marketing-solutions/ads?trk=n_nav_ads_rr_b&amp;src=li-nav","title":{"textDirection":"USER_LOCALE","text":"Marketing Solutions","attributesV2":[],"accessibilityTextAttributesV2":[],"accessibilityText":null,"$recipeTypes":["com.linkedin.566376561ef86249fc89f5596eaf6fe1"],"$type":"com.linkedin.voyager.dash.common.text.TextViewModel"},"$recipeTypes":["com.linkedin.188858304ae14097e59518d245c7cc85"],"$type":"com.linkedin.voyager.dash.feed.nav.BusinessServiceAction"},"description":"Acquire customers and grow your business","$recipeTypes":["com.linkedin.a94ff0919cddaa7056025e9491dc3794"],"$type":"com.linkedin.voyager.dash.feed.nav.BusinessService"},{"businessServiceAction":{"controlName":"nav_business_learning_solutions","actionTarget":"https://learning.linkedin.com/?trk=d_flagship3_nav&amp;veh=learning_solutions&amp;src=li-nav","title":{"textDirection":"USER_LOCALE","text":"Learning Solutions","attributesV2":[],"accessibilityTextAttributesV2":[],"accessibilityText":null,"$recipeTypes":["com.linkedin.566376561ef86249fc89f5596eaf6fe1"],"$type":"com.linkedin.voyager.dash.common.text.TextViewModel"},"$recipeTypes":["com.linkedin.188858304ae14097e59518d245c7cc85"],"$type":"com.linkedin.voyager.dash.feed.nav.BusinessServiceAction"},"description":"Develop talent across your organization","$recipeTypes":["com.linkedin.a94ff0919cddaa7056025e9491dc3794"],"$type":"com.linkedin.voyager.dash.feed.nav.BusinessService"},{"businessServiceAction":{"controlName":"nav_business_admin_center","actionTarget":"https://business.linkedin.com/talent-solutions/customer/admin-center","title":{"textDirection":"USER_LOCALE","text":"Admin Center","attributesV2":[],"accessibilityTextAttributesV2":[],"accessibilityText":null,"$recipeTypes":["com.linkedin.566376561ef86249fc89f5596eaf6fe1"],"$type":"com.linkedin.voyager.dash.common.text.TextViewModel"},"$recipeTypes":["com.linkedin.188858304ae14097e59518d245c7cc85"],"$type":"com.linkedin.voyager.dash.feed.nav.BusinessServiceAction"},"description":"Manage billing and account details","$recipeTypes":["com.linkedin.a94ff0919cddaa7056025e9491dc3794"],"$type":"com.linkedin.voyager.dash.feed.nav.BusinessService"}],"productItemsTitle":{"textDirection":"USER_LOCALE","text":"Visit More LinkedIn Products","attributesV2":[],"accessibilityTextAttributesV2":[],"accessibilityText":null,"$recipeTypes":["com.linkedin.566376561ef86249fc89f5596eaf6fe1"],"$type":"com.linkedin.voyager.dash.common.text.TextViewModel"},"businessServicesTitle":"LinkedIn Business Services","businessServiceActions":[{"controlName":"nav_business_create_company","actionTarget":"https://www.linkedin.com/company/setup/new/","title":{"textDirection":"USER_LOCALE","text":"Create a Company Page  ","attributesV2":[{"start":22,"length":1,"detailData":{"jobPostingName":null,"hyperlink":null,"profileFamiliarName":null,"color":null,"companyName":null,"icon":"IC_PLUS_16DP","epoch":null,"systemImage":null,"textLink":null,"listItemStyle":null,"groupName":null,"hyperlinkOpenExternally":null,"listStyle":null,"profileFullName":null,"stringFieldReference":null,"learningCourseName":null,"profileMention":null,"style":null,"schoolName":null,"hashtag":null},"$recipeTypes":["com.linkedin.9d1c9f8db73cc268b525043481708082"],"$type":"com.linkedin.voyager.dash.common.text.TextAttribute"}],"accessibilityTextAttributesV2":[],"accessibilityText":null,"$recipeTypes":["com.linkedin.566376561ef86249fc89f5596eaf6fe1"],"$type":"com.linkedin.voyager.dash.common.text.TextViewModel"},"$recipeTypes":["com.linkedin.188858304ae14097e59518d245c7cc85"],"$type":"com.linkedin.voyager.dash.feed.nav.BusinessServiceAction"}],"controlName":"nav_launcher","icon":{"attributes":[{"scalingType":null,"detailData":{"profilePictureWithoutFrame":null,"profilePictureWithRingStatus":null,"companyLogo":null,"icon":"IC_NAV_SMALL_APP_SWITCHER_24DP","systemImage":null,"nonEntityGroupLogo":null,"vectorImage":null,"nonEntityProfessionalEventLogo":null,"profilePicture":null,"imageUrl":null,"professionalEventLogo":null,"nonEntityCompanyLogo":null,"nonEntitySchoolLogo":null,"groupLogo":null,"schoolLogo":null,"ghostImage":null,"nonEntityProfilePicture":null},"tintColor":null,"$recipeTypes":["com.linkedin.e6506ba5f5cc1a9b5124781a3661a7db"],"tapTargets":[],"displayAspectRatio":null,"$type":"com.linkedin.voyager.dash.common.image.ImageAttribute"}],"actionTarget":null,"accessibilityTextAttributes":[],"totalCount":null,"accessibilityText":null,"$recipeTypes":["com.linkedin.f89edd0cdc11632a12f86e550f2f5e46"],"$type":"com.linkedin.voyager.dash.common.image.ImageViewModel"},"text":"For Business","$recipeTypes":["com.linkedin.f94aca2770a997f8a58dfb7d6154954a"],"$type":"com.linkedin.voyager.dash.feed.nav.AppLauncher"},"meMenu":null,"navItem":null}],"$type":"com.linkedin.voyager.dash.feed.nav.GlobalNav"},"$recipeTypes":["com.linkedin.1f89c60d56117f36dc02eb3d95a6504d"],"$type":"com.linkedin.1f89c60d56117f36dc02eb3d95a6504d"},"extensions":{"webMetadata":{}}},"meta":{"microSchema":{"isGraphQL":true,"version":"2.1","types":{"com.linkedin.dcb85e1ca353361cb2b5f6fa24a1c9af":{"fields":{"groupUrn":{"type":"string"},"vectorImage":{"type":"com.linkedin.ca116024396bd29dd1345ad0998a57d5"},"group":{"resolvedFrom":"groupUrn","type":"com.linkedin.6c29a299f640b6e802d15141c355bd92"}},"baseType":"com.linkedin.voyager.dash.common.image.NonEntityGroupLogo"},"com.linkedin.1e797f68b521546886989869c5b44a2d":{"fields":{"name":{"type":"string"},"logo":{"type":{"union":{"url":"com.linkedin.common.Url","vectorImage":"com.linkedin.ca116024396bd29dd1345ad0998a57d5"}}},"logoResolutionResult":{"derivedFrom":"logo","type":{"union":{"url":"com.linkedin.common.Url","vectorImage":"com.linkedin.ca116024396bd29dd1345ad0998a57d5"}}},"entityUrn":{"type":"com.linkedin.voyager.dash.common.SchoolUrn"}},"baseType":"com.linkedin.voyager.dash.organization.School"},"com.linkedin.6cf7727c816c79567a0564982ee35ef4":{"fields":{"entityUrn":{"type":"com.linkedin.voyager.dash.common.PremiumUpsellSlotUrn"},"upsellCard":{"type":"com.linkedin.8b2657e6d402c000382bd65eb94ba628"}},"baseType":"com.linkedin.voyager.dash.premium.PremiumUpsellSlotContent"},"com.linkedin.fb4511fb6c2df4a805ef662367e15026":{"fields":{"controlName":{"type":"com.linkedin.voyager.dash.common.tracking.ControlName"},"actionTarget":{"type":"com.linkedin.common.Url"},"text":{"type":"com.linkedin.566376561ef86249fc89f5596eaf6fe1"},"quickHelp":{"type":"boolean"}},"baseType":"com.linkedin.voyager.dash.feed.nav.MeItem"},"com.linkedin.f1332bd87cf4dccab8aa4b4583ad44be":{"fields":{"width":{"type":"int"},"fileIdentifyingUrlPathSegment":{"type":"string"},"expiresAt":{"type":"com.linkedin.common.Time"},"height":{"type":"int"}},"baseType":"com.linkedin.common.VectorArtifact"},"com.linkedin.61dcef34ee68ce7a34919062297c038b":{"fields":{"ringContentType":{"type":"com.linkedin.voyager.dash.common.image.RingContentType"},"actionTarget":{"type":"com.linkedin.common.Url"},"preDashEntityUrn":{"type":"com.linkedin.voyager.dash.common.PreDashUrn"},"entityUrn":{"type":"com.linkedin.voyager.dash.common.RingStatusUrn"},"emphasized":{"type":"boolean"}},"baseType":"com.linkedin.voyager.dash.common.image.RingStatus"},"com.linkedin.6c29a299f640b6e802d15141c355bd92":{"fields":{"name":{"type":"string"},"logo":{"type":{"union":{"url":"com.linkedin.common.Url","vectorImage":"com.linkedin.ca116024396bd29dd1345ad0998a57d5"}}},"logoResolutionResult":{"derivedFrom":"logo","type":{"union":{"url":"com.linkedin.common.Url","vectorImage":"com.linkedin.ca116024396bd29dd1345ad0998a57d5"}}},"entityUrn":{"type":"com.linkedin.voyager.dash.common.GroupUrn"}},"baseType":"com.linkedin.voyager.dash.groups.Group"},"com.linkedin.566376561ef86249fc89f5596eaf6fe1":{"fields":{"textDirection":{"type":"com.linkedin.voyager.dash.common.text.TextDirection"},"attributesV2":{"type":{"array":"com.linkedin.9d1c9f8db73cc268b525043481708082"}},"text":{"type":"string"},"accessibilityTextAttributesV2":{"type":{"array":"com.linkedin.9d1c9f8db73cc268b525043481708082"}},"accessibilityText":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.common.text.TextViewModel"},"com.linkedin.f89edd0cdc11632a12f86e550f2f5e46":{"fields":{"attributes":{"type":{"array":"com.linkedin.e6506ba5f5cc1a9b5124781a3661a7db"}},"actionTarget":{"type":"com.linkedin.common.Url"},"accessibilityTextAttributes":{"type":{"array":"com.linkedin.9d1c9f8db73cc268b525043481708082"}},"totalCount":{"type":"int"},"accessibilityText":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.common.image.ImageViewModel"},"com.linkedin.1f89c60d56117f36dc02eb3d95a6504d":{"fields":{"feedDashGlobalNavs":{"type":"com.linkedin.eae2ed6e463973c8e0d55baecd814363"}},"baseType":"com.linkedin.graphql.Query"},"com.linkedin.bb35e914e880d9f9ad79d52bf644c44c":{"fields":{"title":{"type":"string"},"meItemsUnions":{"type":{"array":{"union":{"meItem":"com.linkedin.fb4511fb6c2df4a805ef662367e15026","premiumUpsellSlotUrn":"string"}}}},"meItems":{"resolvedFrom":"meItemsUnions","type":{"array":{"union":{"meItem":"com.linkedin.fb4511fb6c2df4a805ef662367e15026","premiumUpsellSlotUrn":"com.linkedin.6cf7727c816c79567a0564982ee35ef4"}}}}},"baseType":"com.linkedin.voyager.dash.feed.nav.MeGroup"},"com.linkedin.1112232e110fbaf9f6866335ae420a21":{"fields":{"type":{"type":"com.linkedin.voyager.dash.common.text.ListStyleType"},"index":{"type":"int"}},"baseType":"com.linkedin.voyager.dash.common.text.ListItemStyle"},"com.linkedin.0d2a5c07095246fc3e756f3e922d8aa0":{"fields":{"logoImage":{"type":{"union":{"url":"com.linkedin.common.Url","vectorImage":"com.linkedin.ca116024396bd29dd1345ad0998a57d5"}}},"logoImageResolutionResult":{"derivedFrom":"logoImage","type":{"union":{"url":"com.linkedin.common.Url","vectorImage":"com.linkedin.ca116024396bd29dd1345ad0998a57d5"}}},"entityUrn":{"type":"com.linkedin.voyager.dash.common.ProfessionalEventUrn"}},"baseType":"com.linkedin.voyager.dash.events.ProfessionalEvent"},"com.linkedin.bda725ec0f4ddc7380fb44de84e29723":{"fields":{"displayImageWithFrameReferenceUnion":{"type":{"union":{"url":"com.linkedin.common.Url","vectorImage":"com.linkedin.ca116024396bd29dd1345ad0998a57d5"}}},"displayImageReferenceResolutionResult":{"derivedFrom":"displayImageReference","type":{"union":{"url":"com.linkedin.common.Url","vectorImage":"com.linkedin.ca116024396bd29dd1345ad0998a57d5"}}},"displayImageWithFrameReference":{"derivedFrom":"displayImageWithFrameReferenceUnion","type":{"union":{"url":"com.linkedin.common.Url","vectorImage":"com.linkedin.ca116024396bd29dd1345ad0998a57d5"}}},"displayImageReference":{"type":{"union":{"url":"com.linkedin.common.Url","vectorImage":"com.linkedin.ca116024396bd29dd1345ad0998a57d5"}}},"displayImageUrn":{"type":"com.linkedin.common.Urn"}},"baseType":"com.linkedin.voyager.dash.identity.profile.PhotoFilterPicture"},"com.linkedin.2b5530b88c12ba36048beee3aca27737":{"fields":{"name":{"type":"string"},"logo":{"type":{"union":{"url":"com.linkedin.common.Url","vectorImage":"com.linkedin.ca116024396bd29dd1345ad0998a57d5"}}},"logoResolutionResult":{"derivedFrom":"logo","type":{"union":{"url":"com.linkedin.common.Url","vectorImage":"com.linkedin.ca116024396bd29dd1345ad0998a57d5"}}},"entityUrn":{"type":"com.linkedin.voyager.dash.common.CompanyUrn"},"url":{"type":"com.linkedin.common.Url"}},"baseType":"com.linkedin.voyager.dash.organization.Company"},"com.linkedin.b2c03744140a6cd6a2e693c32790988c":{"fields":{"staticIcon":{"type":"com.linkedin.f89edd0cdc11632a12f86e550f2f5e46"},"activeIcon":{"type":"com.linkedin.f89edd0cdc11632a12f86e550f2f5e46"},"hasCoachmark":{"type":"boolean"},"controlName":{"type":"com.linkedin.voyager.dash.common.tracking.ControlName"},"showIconBorder":{"type":"boolean"},"text":{"type":"string"},"actionTarget":{"type":"com.linkedin.common.Url"},"hasPaid":{"type":"boolean"}},"baseType":"com.linkedin.voyager.dash.feed.nav.NavElement"},"com.linkedin.feccefa74b57bf711c74d0b09805c9f6":{"fields":{"type":{"type":"com.linkedin.voyager.dash.common.text.EpochFormat"},"epochAt":{"type":"com.linkedin.common.Time"}},"baseType":"com.linkedin.voyager.dash.common.text.EpochTime"},"com.linkedin.1febda95b00bfc8c540a7af0dc75a88a":{"fields":{"title":{"type":"string"},"entityUrn":{"type":"com.linkedin.voyager.dash.common.JobPostingUrn"}},"baseType":"com.linkedin.voyager.dash.jobs.JobPosting"},"com.linkedin.65deee184b56ce21c8d7d30fec6acfe4":{"fields":{"urn":{"type":"com.linkedin.common.Urn"},"modelName":{"type":"string"},"fieldName":{"type":"string"},"value":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.common.StringFieldReference"},"com.linkedin.188858304ae14097e59518d245c7cc85":{"fields":{"title":{"type":"com.linkedin.566376561ef86249fc89f5596eaf6fe1"},"controlName":{"type":"com.linkedin.voyager.dash.common.tracking.ControlName"},"actionTarget":{"type":"com.linkedin.common.Url"}},"baseType":"com.linkedin.voyager.dash.feed.nav.BusinessServiceAction"},"com.linkedin.371c4584dc45b7919c4eb6ed6697e8cf":{"fields":{"professionalEvent":{"resolvedFrom":"professionalEventUrn","type":"com.linkedin.0d2a5c07095246fc3e756f3e922d8aa0"},"vectorImage":{"type":"com.linkedin.ca116024396bd29dd1345ad0998a57d5"},"professionalEventUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.common.image.NonEntityProfessionalEventLogo"},"com.linkedin.550a9af095fffdd7fc0f6ceb8743a141":{"fields":{"originalImageUrl":{"type":"com.linkedin.common.Url"},"originalHeight":{"type":"int"},"originalWidth":{"type":"int"},"url":{"type":"com.linkedin.common.Url"}},"baseType":"com.linkedin.voyager.dash.common.ImageUrl"},"com.linkedin.1c710707068d7b33bcbee05036904a3b":{"fields":{"ringStatus":{"type":"com.linkedin.61dcef34ee68ce7a34919062297c038b"},"profileUrn":{"type":"string"},"vectorImage":{"type":"com.linkedin.ca116024396bd29dd1345ad0998a57d5"},"profile":{"resolvedFrom":"profileUrn","type":"com.linkedin.c8b3cc209fc06180b17a4ffb72120344"}},"baseType":"com.linkedin.voyager.dash.common.image.NonEntityProfilePicture"},"com.linkedin.8b2657e6d402c000382bd65eb94ba628":{"fields":{"image":{"type":"com.linkedin.f89edd0cdc11632a12f86e550f2f5e46"},"socialProofInsight":{"type":"com.linkedin.ae72a2e8f27d029e18d8e6d4350b0273"},"ctaText":{"type":"com.linkedin.566376561ef86249fc89f5596eaf6fe1"},"upsellOrderOrigin":{"type":"string"},"controlName":{"type":"com.linkedin.voyager.dash.common.tracking.ControlName"},"actionUrl":{"type":"com.linkedin.common.Url"},"legoTrackingToken":{"type":"string"},"title":{"type":"com.linkedin.566376561ef86249fc89f5596eaf6fe1"},"cancelCta":{"type":"com.linkedin.513969f6493543c4ad7f04b46c3b67f6"},"promotionLegoTrackingToken":{"type":"string"},"funnelCommonHeader":{"type":"com.linkedin.f58e91c23e63f52ceb12bd0fab3eb07b"},"fireDiscoveryImpressionEvent":{"type":"boolean"},"subtitle":{"type":"com.linkedin.566376561ef86249fc89f5596eaf6fe1"},"dismissible":{"type":"boolean"},"layoutStyle":{"type":"com.linkedin.voyager.dash.premium.PremiumUpsellLayoutStyle"},"ctaButtonSecondaryEmphasizedTheme":{"type":"boolean"}},"baseType":"com.linkedin.voyager.dash.premium.PremiumUpsellCard"},"com.linkedin.44f2985bd25b663c32c3c4d4ec070248":{"fields":{"title":{"type":"string"},"entityUrn":{"type":"com.linkedin.voyager.dash.common.LearningCourseUrn"}},"baseType":"com.linkedin.voyager.dash.learning.LearningCourse"},"com.linkedin.ae72a2e8f27d029e18d8e6d4350b0273":{"fields":{"image":{"type":"com.linkedin.f89edd0cdc11632a12f86e550f2f5e46"},"text":{"type":"com.linkedin.566376561ef86249fc89f5596eaf6fe1"}},"baseType":"com.linkedin.voyager.dash.common.ux.InsightViewModel"},"com.linkedin.d66f0cb7963e0345d3ff893927e60c88":{"fields":{"stickerLinkViewUnion":{"type":{"union":{"mediumTemplate":"com.linkedin.637f09655a21b1df5a03c68636fd2d18","largeTemplate":"com.linkedin.1bcf1aba50ed23a46d11fe327f319b18","smallTemplate":"com.linkedin.f223abd9a48757f8395ac497a91593f3"}}},"stickerLinkTemplateSize":{"type":"com.linkedin.voyager.dash.common.media.StickerLinkTemplateSize"},"firstCornerXOffsetPercentage":{"type":"float"},"type":{"type":"com.linkedin.voyager.dash.common.TapTargetAttributeType"},"thirdCornerYOffsetPercentage":{"type":"float"},"url":{"type":"com.linkedin.common.Url"},"stickerLinkView":{"derivedFrom":"stickerLinkViewUnion","type":{"union":{"mediumTemplate":"com.linkedin.637f09655a21b1df5a03c68636fd2d18","largeTemplate":"com.linkedin.1bcf1aba50ed23a46d11fe327f319b18","smallTemplate":"com.linkedin.f223abd9a48757f8395ac497a91593f3"}}},"urn":{"type":"com.linkedin.common.Urn"},"thirdCornerXOffsetPercentage":{"type":"float"},"secondCornerYOffsetPercentage":{"type":"float"},"fourthCornerXOffsetPercentage":{"type":"float"},"firstCornerYOffsetPercentage":{"type":"float"},"untaggable":{"type":"boolean"},"rank":{"type":"int"},"fourthCornerYOffsetPercentage":{"type":"float"},"text":{"type":"string"},"secondCornerXOffsetPercentage":{"type":"float"}},"baseType":"com.linkedin.voyager.dash.common.TapTarget"},"com.linkedin.10f415928dc4647be1fe1eebc72fe277":{"fields":{"entityUrn":{"type":"com.linkedin.voyager.dash.common.HashtagUrn"},"trackingUrn":{"type":"com.linkedin.common.Urn"},"actionTarget":{"type":"com.linkedin.common.Url"}},"baseType":"com.linkedin.voyager.dash.feed.Hashtag"},"com.linkedin.c7f876e8e9f8a631b2896f62a656ce64":{"fields":{"type":{"type":"com.linkedin.voyager.dash.feed.nav.NavType"},"navContent":{"resolvedFrom":"navContentUnion","type":{"union":{"premiumUpsellSlotUrn":"com.linkedin.6cf7727c816c79567a0564982ee35ef4","navElement":"com.linkedin.b2c03744140a6cd6a2e693c32790988c"}}},"navContentUnion":{"type":{"union":{"premiumUpsellSlotUrn":"string","navElement":"com.linkedin.b2c03744140a6cd6a2e693c32790988c"}}}},"baseType":"com.linkedin.voyager.dash.feed.nav.NavItem"},"com.linkedin.1bcf1aba50ed23a46d11fe327f319b18":{"fields":{"image":{"derivedFrom":"imageUnion","type":{"union":{"url":"com.linkedin.common.Url","vectorImage":"com.linkedin.ca116024396bd29dd1345ad0998a57d5"}}},"nameSupplementaryInfo":{"type":"com.linkedin.566376561ef86249fc89f5596eaf6fe1"},"footerText":{"type":"com.linkedin.566376561ef86249fc89f5596eaf6fe1"},"imageUnion":{"type":{"union":{"url":"com.linkedin.common.Url","vectorImage":"com.linkedin.ca116024396bd29dd1345ad0998a57d5"}}},"backgroundImage":{"derivedFrom":"backgroundImageUnion","type":{"union":{"url":"com.linkedin.common.Url","vectorImage":"com.linkedin.ca116024396bd29dd1345ad0998a57d5"}}},"subHeadline":{"type":"com.linkedin.566376561ef86249fc89f5596eaf6fe1"},"name":{"type":"com.linkedin.566376561ef86249fc89f5596eaf6fe1"},"insightText":{"type":"com.linkedin.566376561ef86249fc89f5596eaf6fe1"},"headline":{"type":"com.linkedin.566376561ef86249fc89f5596eaf6fe1"},"backgroundImageUnion":{"type":{"union":{"url":"com.linkedin.common.Url","vectorImage":"com.linkedin.ca116024396bd29dd1345ad0998a57d5"}}}},"baseType":"com.linkedin.voyager.dash.common.media.StickerLinkLargeTemplateView"},"com.linkedin.96db794fa6a744844b487cfa3e195632":{"fields":{"school":{"resolvedFrom":"schoolUrn","type":"com.linkedin.1e797f68b521546886989869c5b44a2d"},"vectorImage":{"type":"com.linkedin.ca116024396bd29dd1345ad0998a57d5"},"schoolUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.common.image.NonEntitySchoolLogo"},"com.linkedin.eae2ed6e463973c8e0d55baecd814363":{"fields":{"logo":{"type":"com.linkedin.4973670c8e07d9bf8572c4c7f8658e2b"},"primaryItemsUnions":{"type":{"array":{"union":{"appLauncher":"com.linkedin.f94aca2770a997f8a58dfb7d6154954a","navItem":"com.linkedin.c7f876e8e9f8a631b2896f62a656ce64","meMenu":"com.linkedin.73113dd58d976ff22a5e4aa2ca35d21d"}}}},"spotlight":{"type":"com.linkedin.c7f876e8e9f8a631b2896f62a656ce64"},"primaryItems":{"derivedFrom":"primaryItemsUnions","type":{"array":{"union":{"appLauncher":"com.linkedin.f94aca2770a997f8a58dfb7d6154954a","navItem":"com.linkedin.c7f876e8e9f8a631b2896f62a656ce64","meMenu":"com.linkedin.73113dd58d976ff22a5e4aa2ca35d21d"}}}}},"baseType":"com.linkedin.voyager.dash.feed.nav.GlobalNav"},"com.linkedin.9d1c9f8db73cc268b525043481708082":{"fields":{"detailData":{"resolvedFrom":"detailDataUnion","type":{"union":{"jobPostingName":"com.linkedin.1febda95b00bfc8c540a7af0dc75a88a","profileFamiliarName":"com.linkedin.c8b3cc209fc06180b17a4ffb72120344","hyperlink":"com.linkedin.common.Url","color":"com.linkedin.voyager.dash.common.text.TextColor","companyName":"com.linkedin.2b5530b88c12ba36048beee3aca27737","icon":"com.linkedin.voyager.dash.common.ArtDecoIconName","epoch":"com.linkedin.feccefa74b57bf711c74d0b09805c9f6","systemImage":"com.linkedin.voyager.dash.common.SystemImageName","textLink":"com.linkedin.72c1c1091a60c5a77aaadac057a84b54","listItemStyle":"com.linkedin.1112232e110fbaf9f6866335ae420a21","listStyle":"com.linkedin.voyager.dash.common.text.ListStyleType","groupName":"com.linkedin.6c29a299f640b6e802d15141c355bd92","hyperlinkOpenExternally":"com.linkedin.common.Url","stringFieldReference":"com.linkedin.65deee184b56ce21c8d7d30fec6acfe4","profileFullName":"com.linkedin.c8b3cc209fc06180b17a4ffb72120344","learningCourseName":"com.linkedin.44f2985bd25b663c32c3c4d4ec070248","profileMention":"com.linkedin.c8b3cc209fc06180b17a4ffb72120344","style":"com.linkedin.voyager.dash.common.text.TextStyle","schoolName":"com.linkedin.1e797f68b521546886989869c5b44a2d","hashtag":"com.linkedin.10f415928dc4647be1fe1eebc72fe277"}}},"length":{"type":"int"},"start":{"type":"int"},"detailDataUnion":{"type":{"union":{"jobPostingName":"string","profileFamiliarName":"string","hyperlink":"com.linkedin.common.Url","color":"com.linkedin.voyager.dash.common.text.TextColor","companyName":"string","icon":"com.linkedin.voyager.dash.common.ArtDecoIconName","epoch":"com.linkedin.feccefa74b57bf711c74d0b09805c9f6","systemImage":"com.linkedin.voyager.dash.common.SystemImageName","textLink":"com.linkedin.72c1c1091a60c5a77aaadac057a84b54","listItemStyle":"com.linkedin.1112232e110fbaf9f6866335ae420a21","listStyle":"com.linkedin.voyager.dash.common.text.ListStyleType","groupName":"string","hyperlinkOpenExternally":"com.linkedin.common.Url","stringFieldReference":"com.linkedin.65deee184b56ce21c8d7d30fec6acfe4","profileFullName":"string","learningCourseName":"string","profileMention":"string","style":"com.linkedin.voyager.dash.common.text.TextStyle","schoolName":"string","hashtag":"string"}}}},"baseType":"com.linkedin.voyager.dash.common.text.TextAttribute"},"com.linkedin.513969f6493543c4ad7f04b46c3b67f6":{"fields":{"controlName":{"type":"com.linkedin.voyager.dash.common.tracking.ControlName"},"appearance":{"type":"com.linkedin.4ef51bc3dc729207a4f87aa1ac1b37cf"},"openExternally":{"type":"boolean"},"accessibilityText":{"type":"string"},"disable":{"type":"boolean"},"url":{"type":"com.linkedin.common.Url"}},"baseType":"com.linkedin.voyager.dash.premium.PremiumButton"},"com.linkedin.f94aca2770a997f8a58dfb7d6154954a":{"fields":{"showDivider":{"type":"boolean"},"productItems":{"type":{"array":"com.linkedin.c7f876e8e9f8a631b2896f62a656ce64"}},"productItemsTitle":{"type":"com.linkedin.566376561ef86249fc89f5596eaf6fe1"},"businessServices":{"type":{"array":"com.linkedin.a94ff0919cddaa7056025e9491dc3794"}},"businessServicesTitle":{"type":"string"},"icon":{"type":"com.linkedin.f89edd0cdc11632a12f86e550f2f5e46"},"controlName":{"type":"com.linkedin.voyager.dash.common.tracking.ControlName"},"businessServiceActions":{"type":{"array":"com.linkedin.188858304ae14097e59518d245c7cc85"}},"text":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.feed.nav.AppLauncher"},"com.linkedin.a94ff0919cddaa7056025e9491dc3794":{"fields":{"businessServiceAction":{"type":"com.linkedin.188858304ae14097e59518d245c7cc85"},"description":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.feed.nav.BusinessService"},"com.linkedin.637f09655a21b1df5a03c68636fd2d18":{"fields":{"name":{"type":"com.linkedin.566376561ef86249fc89f5596eaf6fe1"},"image":{"derivedFrom":"imageUnion","type":{"union":{"url":"com.linkedin.common.Url","vectorImage":"com.linkedin.ca116024396bd29dd1345ad0998a57d5"}}},"nameSupplementaryInfo":{"type":"com.linkedin.566376561ef86249fc89f5596eaf6fe1"},"headline":{"type":"com.linkedin.566376561ef86249fc89f5596eaf6fe1"},"imageUnion":{"type":{"union":{"url":"com.linkedin.common.Url","vectorImage":"com.linkedin.ca116024396bd29dd1345ad0998a57d5"}}},"subHeadline":{"type":"com.linkedin.566376561ef86249fc89f5596eaf6fe1"}},"baseType":"com.linkedin.voyager.dash.common.media.StickerLinkMediumTemplateView"},"com.linkedin.73113dd58d976ff22a5e4aa2ca35d21d":{"fields":{"viewProfileText":{"type":"string"},"controlName":{"type":"com.linkedin.voyager.dash.common.tracking.ControlName"},"text":{"type":"string"},"meGroups":{"type":{"array":"com.linkedin.bb35e914e880d9f9ad79d52bf644c44c"}},"profileUrn":{"type":"string"},"profile":{"resolvedFrom":"profileUrn","type":"com.linkedin.c8b3cc209fc06180b17a4ffb72120344"}},"baseType":"com.linkedin.voyager.dash.feed.nav.MeMenu"},"com.linkedin.f223abd9a48757f8395ac497a91593f3":{"fields":{"name":{"type":"com.linkedin.566376561ef86249fc89f5596eaf6fe1"},"imageUnion":{"type":{"union":{"url":"com.linkedin.common.Url","vectorImage":"com.linkedin.ca116024396bd29dd1345ad0998a57d5"}}},"image":{"derivedFrom":"imageUnion","type":{"union":{"url":"com.linkedin.common.Url","vectorImage":"com.linkedin.ca116024396bd29dd1345ad0998a57d5"}}}},"baseType":"com.linkedin.voyager.dash.common.media.StickerLinkSmallTemplateView"},"com.linkedin.c8b3cc209fc06180b17a4ffb72120344":{"fields":{"profilePicture":{"type":"com.linkedin.bda725ec0f4ddc7380fb44de84e29723"},"lastName":{"type":"string"},"firstName":{"type":"string"},"headline":{"type":"string"},"publicIdentifier":{"type":"string"},"entityUrn":{"type":"com.linkedin.voyager.dash.common.ProfileUrn"}},"baseType":"com.linkedin.voyager.dash.identity.profile.Profile"},"com.linkedin.4ef51bc3dc729207a4f87aa1ac1b37cf":{"fields":{"premiumStyle":{"type":"boolean"},"size":{"type":"com.linkedin.voyager.dash.common.ux.button.ButtonSize"},"icon":{"type":"com.linkedin.voyager.dash.common.SystemImageName"},"text":{"type":"string"},"iconAfterText":{"type":"boolean"},"emphasize":{"type":"boolean"},"category":{"type":"com.linkedin.voyager.dash.common.ux.button.ButtonCategory"}},"baseType":"com.linkedin.voyager.dash.common.ux.button.ButtonAppearance"},"com.linkedin.e6506ba5f5cc1a9b5124781a3661a7db":{"fields":{"detailData":{"resolvedFrom":"detailDataUnion","type":{"union":{"profilePictureWithoutFrame":"com.linkedin.c8b3cc209fc06180b17a4ffb72120344","profilePictureWithRingStatus":"com.linkedin.c8b3cc209fc06180b17a4ffb72120344","companyLogo":"com.linkedin.2b5530b88c12ba36048beee3aca27737","icon":"com.linkedin.voyager.dash.common.ArtDecoIconName","systemImage":"com.linkedin.voyager.dash.common.SystemImageName","nonEntityGroupLogo":"com.linkedin.dcb85e1ca353361cb2b5f6fa24a1c9af","vectorImage":"com.linkedin.ca116024396bd29dd1345ad0998a57d5","nonEntityProfessionalEventLogo":"com.linkedin.371c4584dc45b7919c4eb6ed6697e8cf","profilePicture":"com.linkedin.c8b3cc209fc06180b17a4ffb72120344","imageUrl":"com.linkedin.550a9af095fffdd7fc0f6ceb8743a141","professionalEventLogo":"com.linkedin.0d2a5c07095246fc3e756f3e922d8aa0","nonEntitySchoolLogo":"com.linkedin.96db794fa6a744844b487cfa3e195632","nonEntityCompanyLogo":"com.linkedin.72e4cd594b8572e0ec9ddb034eafc088","schoolLogo":"com.linkedin.1e797f68b521546886989869c5b44a2d","groupLogo":"com.linkedin.6c29a299f640b6e802d15141c355bd92","ghostImage":"com.linkedin.voyager.dash.common.image.GhostImageType","nonEntityProfilePicture":"com.linkedin.1c710707068d7b33bcbee05036904a3b"}}},"tintColor":{"type":"com.linkedin.voyager.dash.common.SystemImageTintColor"},"detailDataUnion":{"type":{"union":{"profilePictureWithoutFrame":"string","profilePictureWithRingStatus":"string","companyLogo":"string","icon":"com.linkedin.voyager.dash.common.ArtDecoIconName","systemImage":"com.linkedin.voyager.dash.common.SystemImageName","nonEntityGroupLogo":"com.linkedin.dcb85e1ca353361cb2b5f6fa24a1c9af","vectorImage":"com.linkedin.ca116024396bd29dd1345ad0998a57d5","nonEntityProfessionalEventLogo":"com.linkedin.371c4584dc45b7919c4eb6ed6697e8cf","profilePicture":"string","imageUrl":"com.linkedin.550a9af095fffdd7fc0f6ceb8743a141","professionalEventLogo":"string","nonEntitySchoolLogo":"com.linkedin.96db794fa6a744844b487cfa3e195632","nonEntityCompanyLogo":"com.linkedin.72e4cd594b8572e0ec9ddb034eafc088","schoolLogo":"string","groupLogo":"string","ghostImage":"com.linkedin.voyager.dash.common.image.GhostImageType","nonEntityProfilePicture":"com.linkedin.1c710707068d7b33bcbee05036904a3b"}}},"tapTargets":{"type":{"array":"com.linkedin.d66f0cb7963e0345d3ff893927e60c88"}},"scalingType":{"type":"com.linkedin.voyager.dash.common.image.ScalingType"},"displayAspectRatio":{"type":"double"}},"baseType":"com.linkedin.voyager.dash.common.image.ImageAttribute"},"com.linkedin.ca116024396bd29dd1345ad0998a57d5":{"fields":{"attribution":{"type":"string"},"digitalmediaAsset":{"type":"com.linkedin.common.DigitalmediaAssetUrn"},"rootUrl":{"type":"string"},"artifacts":{"type":{"array":"com.linkedin.f1332bd87cf4dccab8aa4b4583ad44be"}}},"baseType":"com.linkedin.common.VectorImage"},"com.linkedin.72c1c1091a60c5a77aaadac057a84b54":{"fields":{"viewingBehavior":{"type":"com.linkedin.voyager.dash.common.ux.UrlViewingBehavior"},"url":{"type":"com.linkedin.common.Url"}},"baseType":"com.linkedin.voyager.dash.common.text.TextLink"},"com.linkedin.72e4cd594b8572e0ec9ddb034eafc088":{"fields":{"companyUrn":{"type":"string"},"company":{"resolvedFrom":"companyUrn","type":"com.linkedin.2b5530b88c12ba36048beee3aca27737"},"vectorImage":{"type":"com.linkedin.ca116024396bd29dd1345ad0998a57d5"}},"baseType":"com.linkedin.voyager.dash.common.image.NonEntityCompanyLogo"},"com.linkedin.f58e91c23e63f52ceb12bd0fab3eb07b":{"fields":{"utype":{"type":"string"},"referenceId":{"type":"com.linkedin.common.TrackingId"}},"baseType":"com.linkedin.voyager.dash.premium.PremiumFunnelCommonHeader"},"com.linkedin.4973670c8e07d9bf8572c4c7f8658e2b":{"fields":{"controlName":{"type":"com.linkedin.voyager.dash.common.tracking.ControlName"},"logo":{"type":"com.linkedin.f89edd0cdc11632a12f86e550f2f5e46"},"hoverText":{"type":"com.linkedin.566376561ef86249fc89f5596eaf6fe1"}},"baseType":"com.linkedin.voyager.dash.feed.nav.BrandingLogo"}}}},"included":[{"firstName":"Harith","lastName":"Al-Safi","profilePicture":{"displayImageReferenceResolutionResult":{"url":null,"vectorImage":{"digitalmediaAsset":null,"attribution":null,"$recipeTypes":["com.linkedin.ca116024396bd29dd1345ad0998a57d5"],"artifacts":[{"width":100,"$recipeTypes":["com.linkedin.f1332bd87cf4dccab8aa4b4583ad44be"],"fileIdentifyingUrlPathSegment":"100_100/0/1675373176223?e=1691625600&amp;v=beta&amp;t=-3k4RuOJvA8N9zuEKPE4wNyFxg7L6jKBLgCDUEe33ec","expiresAt":1691625600000,"height":100,"$type":"com.linkedin.common.VectorArtifact"},{"width":200,"$recipeTypes":["com.linkedin.f1332bd87cf4dccab8aa4b4583ad44be"],"fileIdentifyingUrlPathSegment":"200_200/0/1675373176223?e=1691625600&amp;v=beta&amp;t=_9o-z2z8w540NQAt4gMeniczzyyKkD0PQPcIiPgetgo","expiresAt":1691625600000,"height":200,"$type":"com.linkedin.common.VectorArtifact"},{"width":400,"$recipeTypes":["com.linkedin.f1332bd87cf4dccab8aa4b4583ad44be"],"fileIdentifyingUrlPathSegment":"400_400/0/1675373176223?e=1691625600&amp;v=beta&amp;t=OfegiYnmbSi2ez4L2Z9exoHtI1j77ximISKDtpMfBeM","expiresAt":1691625600000,"height":400,"$type":"com.linkedin.common.VectorArtifact"},{"width":800,"$recipeTypes":["com.linkedin.f1332bd87cf4dccab8aa4b4583ad44be"],"fileIdentifyingUrlPathSegment":"800_800/0/1675373176223?e=1691625600&amp;v=beta&amp;t=m1XIXW9S_uGc_fY4J_eZopCMpeJbO484Aha0oGVAeY8","expiresAt":1691625600000,"height":800,"$type":"com.linkedin.common.VectorArtifact"}],"rootUrl":"https://media.licdn.com/dms/image/D4E03AQGB3OP3rlsmtQ/profile-displayphoto-shrink_","$type":"com.linkedin.common.VectorImage"}},"displayImageWithFrameReference":null,"$recipeTypes":["com.linkedin.bda725ec0f4ddc7380fb44de84e29723"],"$type":"com.linkedin.voyager.dash.identity.profile.PhotoFilterPicture"},"entityUrn":"urn:li:fsd_profile:ACoAAC9P7scB1yv1hA-ZjtKBAxcuNQvmvu08uhI","headline":"Software Engineer | Computer Engineer | AI Enthusiast ","publicIdentifier":"harith-al-safi","$recipeTypes":["com.linkedin.c8b3cc209fc06180b17a4ffb72120344"],"$type":"com.linkedin.voyager.dash.identity.profile.Profile"},{"entityUrn":"urn:li:fsd_premiumUpsellSlot:NAV_SPOTLIGHT","$recipeTypes":["com.linkedin.6cf7727c816c79567a0564982ee35ef4"],"upsellCard":{"image":null,"socialProofInsight":null,"upsellOrderOrigin":"premium_nav_upsell_text","ctaText":{"textDirection":"USER_LOCALE","text":"Get Hired Faster, Try Premium Free","attributesV2":[],"accessibilityTextAttributesV2":[],"accessibilityText":null,"$recipeTypes":["com.linkedin.566376561ef86249fc89f5596eaf6fe1"],"$type":"com.linkedin.voyager.dash.common.text.TextViewModel"},"actionUrl":"https://www.linkedin.com/premium/products/?family=JSS&amp;upsellOrderOrigin=premium_nav_upsell_text&amp;intentType=SEEK_JOB&amp;utype=job&amp;referenceId=%2FjM4QestQTuPyrwvSo4HnA%3D%3D","controlName":"premium_nav_upsell_text_click","legoTrackingToken":null,"title":null,"$recipeTypes":["com.linkedin.8b2657e6d402c000382bd65eb94ba628"],"$type":"com.linkedin.voyager.dash.premium.PremiumUpsellCard","cancelCta":null,"promotionLegoTrackingToken":null,"funnelCommonHeader":{"utype":null,"$recipeTypes":["com.linkedin.f58e91c23e63f52ceb12bd0fab3eb07b"],"referenceId":"þ38Aë-A;Ê¼/J\u0007","$type":"com.linkedin.voyager.dash.premium.PremiumFunnelCommonHeader"},"fireDiscoveryImpressionEvent":false,"subtitle":null,"dismissible":false,"layoutStyle":"CUSTOM","ctaButtonSecondaryEmphasizedTheme":false},"$type":"com.linkedin.voyager.dash.premium.PremiumUpsellSlotContent"},{"entityUrn":"urn:li:fsd_premiumUpsellSlot:NAV_ME","$recipeTypes":["com.linkedin.6cf7727c816c79567a0564982ee35ef4"],"upsellCard":{"image":null,"socialProofInsight":null,"upsellOrderOrigin":"premium_nav_me_upsell","ctaText":{"textDirection":"USER_LOCALE","text":"Try Premium for free","attributesV2":[],"accessibilityTextAttributesV2":[],"accessibilityText":null,"$recipeTypes":["com.linkedin.566376561ef86249fc89f5596eaf6fe1"],"$type":"com.linkedin.voyager.dash.common.text.TextViewModel"},"actionUrl":"https://www.linkedin.com/premium/products/?upsellOrderOrigin=premium_nav_me_upsell&amp;referenceId=lPS%2F1xj5TauUPsp1alSAmw%3D%3D","controlName":"premium_nav_me_upsell_click","legoTrackingToken":null,"title":null,"$recipeTypes":["com.linkedin.8b2657e6d402c000382bd65eb94ba628"],"$type":"com.linkedin.voyager.dash.premium.PremiumUpsellCard","cancelCta":null,"promotionLegoTrackingToken":null,"funnelCommonHeader":{"utype":null,"$recipeTypes":["com.linkedin.f58e91c23e63f52ceb12bd0fab3eb07b"],"referenceId":"ô¿×\u0018ùM«&gt;ÊujT","$type":"com.linkedin.voyager.dash.premium.PremiumFunnelCommonHeader"},"fireDiscoveryImpressionEvent":false,"subtitle":null,"dismissible":false,"layoutStyle":"TEXT_LINK","ctaButtonSecondaryEmphasizedTheme":false},"$type":"com.linkedin.voyager.dash.premium.PremiumUpsellSlotContent"}]}
</code>
<code style="display: none" id="datalet-bpr-guid-104262">
  {"request":"/voyager/api/graphql?includeWebMetadata\u003Dtrue\u0026variables\u003D()\u0026\u0026queryId\u003DvoyagerFeedDashGlobalNavs.60b71bbf543884ca067e8712e82e8e7e","status":200,"body":"bpr-guid-104262","method":"GET","headers":{"x-li-uuid":"AAX9pWM/tcB+TnflXcw30Q\u003D\u003D"}}
</code>
<img src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" style="display: none" class="datalet-bpr-guid-104262"><code style="display: none" id="bpr-guid-104263">
  {"data":{"entityUrn":"urn:li:collectionResponse:lU0/k/dVsZn9xmb/UcmEdwyDhb3pts9eUWgS4Ietly8=","elements":[],"paging":{"count":10,"start":0,"links":[]},"$type":"com.linkedin.restli.common.CollectionResponse"},"meta":{"microSchema":{"version":"2","types":{"com.linkedin.deco.recipe.anonymous.Anon1080314395":{"fields":{"ringContentType":{"type":"string"},"actionTarget":{"type":"string"},"preDashEntityUrn":{"type":"string"},"entityUrn":{"type":"string"},"emphasized":{"type":"boolean"}},"baseType":"com.linkedin.voyager.dash.common.image.RingStatus"},"com.linkedin.deco.recipe.anonymous.Anon489758292":{"fields":{"viewer":{"type":"com.linkedin.deco.recipe.anonymous.Anon430310092","resolvedFrom":"viewerUrn"},"contentSeriesUrn":{"type":"string"},"contentSeries":{"type":"com.linkedin.deco.recipe.anonymous.Anon1789236903","resolvedFrom":"contentSeriesUrn"},"viewerUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.relationships.MemberToContentSeriesSubscribeMetadata"},"com.linkedin.deco.recipe.anonymous.Anon712430272":{"fields":{"entityImage":{"type":"com.linkedin.voyager.dash.deco.common.image.ImageViewModel"},"backgroundImage":{"type":"com.linkedin.voyager.dash.deco.common.image.ImageViewModel"},"subtitle":{"type":"com.linkedin.voyager.dash.deco.common.text.TextViewModelV2"},"subDescription":{"type":"com.linkedin.voyager.dash.deco.common.text.TextViewModelV2"},"description":{"type":"com.linkedin.voyager.dash.deco.common.text.TextViewModelV2"},"contentHorizontallyCentered":{"type":"boolean"},"title":{"type":"com.linkedin.voyager.dash.deco.common.text.TextViewModelV2"}},"baseType":"com.linkedin.voyager.dash.sponsoredcontent.leadgen.LeadGenBannerComponent"},"com.linkedin.deco.recipe.anonymous.Anon1479950671":{"fields":{"elements":{"type":{"array":"com.linkedin.deco.recipe.anonymous.Anon2036460800"}}},"baseType":"com.linkedin.restli.common.CollectionResponse"},"com.linkedin.deco.recipe.anonymous.Anon377984030":{"fields":{"professionalEvent":{"type":"com.linkedin.deco.recipe.anonymous.Anon1213723597","resolvedFrom":"professionalEventUrn"},"vectorImage":{"type":"com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrlAndAttribution"},"professionalEventUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.common.image.NonEntityProfessionalEventLogo"},"com.linkedin.voyager.dash.deco.common.image.Company":{"fields":{"logo":{"type":{"union":{"url":"string","vectorImage":"com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrlAndAttribution"}}},"entityUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.organization.Company"},"com.linkedin.voyager.dash.deco.feed.publishing.SubscribeAction":{"fields":{"subscribed":{"type":"boolean"},"preDashEntityUrn":{"type":"string"},"entityUrn":{"type":"string"},"subscriberCount":{"type":"int"}},"baseType":"com.linkedin.voyager.dash.publishing.SubscribeAction"},"com.linkedin.deco.recipe.anonymous.Anon405167834":{"fields":{"name":{"type":"com.linkedin.voyager.dash.deco.common.text.TextViewModelV2"},"nameSupplementaryInfo":{"type":"com.linkedin.voyager.dash.deco.common.text.TextViewModelV2"},"imageUnion":{"type":{"union":{"url":"string","vectorImage":"com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrlAndAttribution"}}},"headline":{"type":"com.linkedin.voyager.dash.deco.common.text.TextViewModelV2"},"subHeadline":{"type":"com.linkedin.voyager.dash.deco.common.text.TextViewModelV2"}},"baseType":"com.linkedin.voyager.dash.common.media.StickerLinkMediumTemplateView"},"com.linkedin.deco.recipe.anonymous.Anon813412436":{"fields":{"questions":{"type":{"array":"com.linkedin.deco.recipe.anonymous.Anon1150537667"}}},"baseType":"com.linkedin.voyager.dash.sponsoredcontent.leadgen.LeadGenFormSection"},"com.linkedin.voyager.dash.deco.launchpad.EdgeBuildingCohortReason":{"fields":{"sourceType":{"type":"string"},"reasonObjects":{"type":{"array":"string"}},"reasonContext":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.launchpad.attribute.EdgeBuildingCohortReason"},"com.linkedin.deco.recipe.anonymous.Anon1444411496":{"fields":{"countryUrn":{"type":"string"},"country":{"type":"com.linkedin.deco.recipe.anonymous.Anon1918694303","resolvedFrom":"countryUrn"},"defaultLocalizedNameWithoutCountryName":{"type":"string"},"entityUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.common.Geo"},"com.linkedin.deco.recipe.anonymous.Anon1226238669":{"fields":{"name":{"type":"string"},"logo":{"type":{"union":{"url":"string","vectorImage":"com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrlAndAttribution"}}},"universalName":{"type":"string"},"entityUrn":{"type":"string"},"url":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.organization.Company"},"com.linkedin.deco.recipe.anonymous.Anon798864187":{"fields":{"influencer":{"type":"boolean"},"entityUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.identity.profile.Profile"},"com.linkedin.voyager.dash.deco.common.ux.StatefulButtonModel":{"fields":{"actionDataModel":{"type":{"union":{"follow":"com.linkedin.voyager.dash.deco.feed.FollowingState","connectionOrInvitation":"com.linkedin.voyager.dash.deco.relationships.MemberRelationshipV2","memberToEntityRelationship":"com.linkedin.voyager.dash.deco.relationships.DirectionalEntityRelationship"}},"resolvedFrom":"actionDataModelUnion"},"actionDataModelUnion":{"type":{"union":{"connectionOrInvitation":"string","relationshipActionData":"com.linkedin.voyager.dash.deco.common.ux.RelationshipActionData","memberToEntityRelationship":"string","follow":"string"}}},"emphasisStyle":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.common.ux.button.StatefulButtonModel"},"com.linkedin.deco.recipe.anonymous.Anon1636615691":{"fields":{"transcripts":{"type":{"array":"string"}},"pagesPerResolution":{"type":{"array":"com.linkedin.deco.recipe.anonymous.Anon1525160909"}}},"baseType":"com.linkedin.documentcontent.DocumentPages"},"com.linkedin.deco.recipe.anonymous.Anon934606613":{"fields":{"type":{"type":"string"},"name":{"type":"string"},"controlName":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.relationships.invitation.InvitationRelationshipOption"},"com.linkedin.voyager.dash.deco.common.TapTargetWithoutEntity":{"fields":{"stickerLinkViewUnion":{"type":{"union":{"mediumTemplate":"com.linkedin.deco.recipe.anonymous.Anon405167834","largeTemplate":"com.linkedin.deco.recipe.anonymous.Anon173266477","smallTemplate":"com.linkedin.deco.recipe.anonymous.Anon655007389"}}},"stickerLinkTemplateSize":{"type":"string"},"firstCornerXOffsetPercentage":{"type":"float"},"type":{"type":"string"},"thirdCornerYOffsetPercentage":{"type":"float"},"url":{"type":"string"},"urn":{"type":"string"},"thirdCornerXOffsetPercentage":{"type":"float"},"secondCornerYOffsetPercentage":{"type":"float"},"fourthCornerXOffsetPercentage":{"type":"float"},"firstCornerYOffsetPercentage":{"type":"float"},"untaggable":{"type":"boolean"},"rank":{"type":"int"},"text":{"type":"string"},"fourthCornerYOffsetPercentage":{"type":"float"},"secondCornerXOffsetPercentage":{"type":"float"}},"baseType":"com.linkedin.voyager.dash.common.TapTarget"},"com.linkedin.deco.recipe.anonymous.Anon173266477":{"fields":{"nameSupplementaryInfo":{"type":"com.linkedin.voyager.dash.deco.common.text.TextViewModelV2"},"footerText":{"type":"com.linkedin.voyager.dash.deco.common.text.TextViewModelV2"},"imageUnion":{"type":{"union":{"url":"string","vectorImage":"com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrlAndAttribution"}}},"subHeadline":{"type":"com.linkedin.voyager.dash.deco.common.text.TextViewModelV2"},"name":{"type":"com.linkedin.voyager.dash.deco.common.text.TextViewModelV2"},"insightText":{"type":"com.linkedin.voyager.dash.deco.common.text.TextViewModelV2"},"headline":{"type":"com.linkedin.voyager.dash.deco.common.text.TextViewModelV2"},"backgroundImageUnion":{"type":{"union":{"url":"string","vectorImage":"com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrlAndAttribution"}}}},"baseType":"com.linkedin.voyager.dash.common.media.StickerLinkLargeTemplateView"},"com.linkedin.deco.recipe.anonymous.Anon1312950162":{"fields":{"entityUrn":{"type":"string"},"memberRelationshipUnion":{"type":{"union":{"self":"com.linkedin.restli.common.EmptyRecord","connection":"com.linkedin.deco.recipe.anonymous.Anon2134644859","noConnection":"com.linkedin.deco.recipe.anonymous.Anon1792705474"}}}},"baseType":"com.linkedin.voyager.dash.relationships.MemberRelationship"},"com.linkedin.voyager.dash.deco.organization.OrganizationPermissions":{"fields":{"canCreateBroadcast":{"type":"boolean"},"canReadContentSuggestions":{"type":"boolean"},"canSeeProducts":{"type":"boolean"},"canUpdateOrganizationProfile":{"type":"boolean"},"canSponsorShare":{"type":"boolean"},"canEditPendingDirectSponsoredContentPosters":{"type":"boolean"},"canReadAdminFeedFollowingPill":{"type":"boolean"},"canUntagFromMention":{"type":"boolean"},"canReadOrganizationActivity":{"type":"boolean"},"canManageCareerPages":{"type":"boolean"},"canAssociateHashtag":{"type":"boolean"},"canDeleteShare":{"type":"boolean"},"canInviteMemberToFollow":{"type":"boolean"},"canEditPipelineBuilderAdministrators":{"type":"boolean"},"canReadBroadcastAnalytics":{"type":"boolean"},"canManageMessagingAccess":{"type":"boolean"},"canMembersInviteToFollow":{"type":"boolean"},"canReadPipelineBuilderAdminPage":{"type":"boolean"},"canDeactivateOrganization":{"type":"boolean"},"canCreateOrganicShare":{"type":"boolean"},"canNotifyEmployeesOfShare":{"type":"boolean"},"canEditDarkShare":{"type":"boolean"},"canSeePostJobButton":{"type":"boolean"},"canEnableCommentsShare":{"type":"boolean"},"canReadOrganizationLeadsAnalytics":{"type":"boolean"},"canDeleteDarkShare":{"type":"boolean"},"canCreateJobPosting":{"type":"boolean"},"canEditLeadGenerationFormManagers":{"type":"boolean"},"canReadMessages":{"type":"boolean"},"canReadOrganizationTalentBrandAnalytics":{"type":"boolean"},"canEditDirectSponsoredContentPosters":{"type":"boolean"},"canPinShare":{"type":"boolean"},"canReadPipelineBuilderAdministrators":{"type":"boolean"},"canCreateLinkedInPagesProductFeedBack":{"type":"boolean"},"canReadEvents":{"type":"boolean"},"organizationRoles":{"type":{"array":"com.linkedin.voyager.dash.deco.organization.OrganizationRoleType"}},"canEditEvents":{"type":"boolean"},"canManageOrganizationalPageFollow":{"type":"boolean"},"canReadOrganizationUpdateAnalytics":{"type":"boolean"},"canCreateComment":{"type":"boolean"},"canRequestAdminAccess":{"type":"boolean"},"canEditAdministrators":{"type":"boolean"},"canCreateDarkShare":{"type":"boolean"},"canEmployeesInviteToFollow":{"type":"boolean"},"canSeeEmployeeExperienceAsMember":{"type":"boolean"},"canReadAdministrators":{"type":"boolean"},"canExportLeads":{"type":"boolean"},"canReadDirectSponsoredContentPosters":{"type":"boolean"},"canCreateShowcase":{"type":"boolean"},"canManageEmployeeExperienceSettings":{"type":"boolean"},"canReadLeadGenerationFormManagers":{"type":"boolean"},"canReadOrganizationVisitorAnalytics":{"type":"boolean"},"canEditCurators":{"type":"boolean"},"canEditProducts":{"type":"boolean"},"canManageVerifiedEmailDomains":{"type":"boolean"},"canReadPendingAdministrators":{"type":"boolean"},"canReadPendingDirectSponsoredContentPosters":{"type":"boolean"},"canEditPipelineBuilderAdminPage":{"type":"boolean"},"canReadTermsAndAgreements":{"type":"boolean"},"canReadOrganizationFollowerAnalytics":{"type":"boolean"},"canManageOrganizationCompetitors":{"type":"boolean"},"canSendMessages":{"type":"boolean"},"canCreateReaction":{"type":"boolean"},"canDisableCommentsShare":{"type":"boolean"},"canEditPendingAdministrators":{"type":"boolean"},"canNotifyEmployees":{"type":"boolean"},"canReadOrganizationPipelineBuilderAnalytics":{"type":"boolean"},"canSeeOrganizationAdministrativePage":{"type":"boolean"}},"baseType":"com.linkedin.voyager.dash.organization.OrganizationPermissions"},"com.linkedin.voyager.dash.deco.common.video.Transcript":{"fields":{"captionFormat":{"type":"string"},"locale":{"type":"com.linkedin.voyager.dash.deco.common.Locale"},"lines":{"type":{"array":"com.linkedin.voyager.dash.deco.common.video.TranscriptLine"}},"isAutogenerated":{"type":"boolean"},"captionFile":{"type":"string"}},"baseType":"com.linkedin.videocontent.Transcript"},"com.linkedin.deco.recipe.anonymous.Anon1286825962":{"fields":{"sharedSecret":{"type":"string"},"entityUrn":{"type":"string"},"invitationId":{"type":"long"}},"baseType":"com.linkedin.voyager.dash.relationships.invitation.Invitation"},"com.linkedin.voyager.dash.deco.common.image.OrganizationalPage":{"fields":{"entityUrn":{"type":"string"},"pageType":{"type":"string"},"logoV2":{"type":"com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrlAndAttribution"}},"baseType":"com.linkedin.voyager.dash.organization.OrganizationalPage"},"com.linkedin.deco.recipe.anonymous.Anon1358424483":{"fields":{"text":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.sponsoredcontent.leadgen.TextFieldComponent"},"com.linkedin.deco.recipe.anonymous.Anon632521550":{"fields":{"entityUrn":{"type":"string"},"joinedAt":{"type":"long"},"profile":{"type":"com.linkedin.deco.recipe.anonymous.Anon437558093","resolvedFrom":"profileUrn"},"groupUrn":{"type":"string"},"preDashEntityUrn":{"type":"string"},"profileUrn":{"type":"string"},"status":{"type":"string"},"group":{"type":"com.linkedin.deco.recipe.anonymous.Anon1869367056","resolvedFrom":"groupUrn"}},"baseType":"com.linkedin.voyager.dash.groups.GroupMembership"},"com.linkedin.deco.recipe.anonymous.Anon879961581":{"fields":{"checked":{"type":"boolean"},"text":{"type":"com.linkedin.voyager.dash.deco.common.text.TextViewModelV2"}},"baseType":"com.linkedin.voyager.dash.sponsoredcontent.leadgen.CheckboxComponent"},"com.linkedin.deco.recipe.anonymous.Anon523036483":{"fields":{"title":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.organization.FollowersMetadata"},"com.linkedin.voyager.dash.deco.common.image.Group":{"fields":{"logo":{"type":{"union":{"url":"string","vectorImage":"com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrlAndAttribution"}}},"entityUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.groups.Group"},"com.linkedin.deco.recipe.anonymous.Anon1918694303":{"fields":{"entityUrn":{"type":"string"},"defaultLocalizedName":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.common.Geo"},"com.linkedin.deco.recipe.anonymous.Anon572127587":{"fields":{"insightViewee":{"type":"com.linkedin.deco.recipe.anonymous.Anon798864187","resolvedFrom":"insightVieweeUrn"},"insightVieweeUrn":{"type":"string"},"entityUrn":{"type":"string"},"sharedConnectionDetailTargetResolutionResult":{"type":"com.linkedin.deco.recipe.anonymous.Anon798864187","resolvedFrom":"sharedConnectionDetailTarget"},"insightImage":{"type":"com.linkedin.voyager.dash.deco.common.image.ImageViewModel"},"sharedConnectionDetailTarget":{"type":"string"},"text":{"type":"com.linkedin.voyager.dash.deco.common.text.TextViewModelV2"},"navigationUrl":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.relationships.Insight"},"com.linkedin.voyager.dash.deco.launchpad.OrganizationTopCardForEntityFollow":{"fields":{"socialProofInsight":{"type":{"union":{"standard":"com.linkedin.deco.recipe.anonymous.Anon572127587","compact":"com.linkedin.deco.recipe.anonymous.Anon853977300"}},"resolvedFrom":"socialProofInsightUnion"},"viewerPermissions":{"type":"com.linkedin.voyager.dash.deco.launchpad.OrganizationPermissions"},"salesNavigatorCompanyUrl":{"type":"string"},"industryV2Taxonomy":{"type":{"map":"com.linkedin.voyager.dash.deco.common.IndustryV2"},"resolvedFrom":"industryV2TaxonomyUrns"},"industry":{"type":{"map":"com.linkedin.voyager.dash.deco.common.Industry"},"resolvedFrom":"industryUrns"},"industryUrns":{"type":{"array":"string"}},"industryV2Urns":{"type":{"array":"string"}},"socialProofInsightUnion":{"type":{"union":{"standard":"string","compact":"string"}}},"employeeCount":{"type":"long"},"associatedSignatureProductUrn":{"type":"string"},"url":{"type":"string"},"callToAction":{"type":"com.linkedin.voyager.dash.deco.launchpad.CallToAction"},"relevanceReason":{"type":"com.linkedin.voyager.dash.deco.common.ux.baseInsightViewModel"},"associatedSignatureProduct":{"type":"com.linkedin.voyager.dash.deco.organization.FullMemberProduct","resolvedFrom":"associatedSignatureProductUrn"},"industryV2":{"type":{"map":"com.linkedin.voyager.dash.deco.common.Industry"},"resolvedFrom":"industryV2Urns"},"industryV2TaxonomyUrns":{"type":{"array":"string"}},"followingStateUrn":{"type":"string"},"entityUrn":{"type":"string"},"followingState":{"type":"com.linkedin.voyager.dash.deco.feed.FollowingState","resolvedFrom":"followingStateUrn"},"name":{"type":"string"},"logo":{"type":{"union":{"url":"string","vectorImage":"com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrlAndAttribution"}}},"universalName":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.organization.Company"},"com.linkedin.deco.recipe.anonymous.Anon1213723597":{"fields":{"entityUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.events.ProfessionalEvent"},"com.linkedin.deco.recipe.anonymous.Anon184130218":{"fields":{"name":{"type":"string"},"logo":{"type":{"union":{"url":"string","vectorImage":"com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrlAndAttribution"}}},"entityUrn":{"type":"string"},"url":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.organization.Company"},"com.linkedin.deco.recipe.anonymous.Anon487759616":{"fields":{"company":{"type":"com.linkedin.deco.recipe.anonymous.Anon1226238669","resolvedFrom":"companyUrn"},"schoolName":{"type":"string"},"school":{"type":"com.linkedin.deco.recipe.anonymous.Anon1621960601","resolvedFrom":"schoolUrn"},"entityUrn":{"type":"string"},"companyUrn":{"type":"string"},"schoolUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.identity.profile.Education"},"com.linkedin.deco.recipe.anonymous.Anon1251747613":{"fields":{"urn":{"type":"string"},"modelName":{"type":"string"},"fieldName":{"type":"string"},"value":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.common.StringFieldReference"},"com.linkedin.voyager.dash.deco.organization.FullMemberProduct":{"fields":{"organizationsUsingProduct":{"type":{"map":"com.linkedin.deco.recipe.anonymous.Anon579987817"},"resolvedFrom":"organizationsUsingProductUrns"},"productUserTitle":{"type":{"map":"com.linkedin.deco.recipe.anonymous.Anon1369245809"},"resolvedFrom":"productUserTitleUrns"},"companyUrn":{"type":"string"},"productUserTitleUrns":{"type":{"array":"string"}},"similarProducts":{"type":"com.linkedin.deco.recipe.anonymous.Anon1361453782","isInjection":true},"entityUrn":{"type":"string"},"organizationalPage":{"type":"com.linkedin.deco.recipe.anonymous.Anon1196575529","resolvedFrom":"organizationalPageUrn"},"logo":{"type":"com.linkedin.voyager.dash.deco.common.image.ImageViewModel"},"similarProductsFromSameOrganization":{"type":"com.linkedin.deco.recipe.anonymous.Anon1994177525","isInjection":true},"company":{"type":"com.linkedin.deco.recipe.anonymous.Anon422795650","resolvedFrom":"companyUrn"},"productCardCallToActionUnion":{"type":{"union":{"organizationProductLeadGenFormCallToAction":"com.linkedin.deco.recipe.anonymous.Anon792975169","organizationProductCallToAction":"com.linkedin.deco.recipe.anonymous.Anon625674184","organizationProductAddSkillCallToAction":"com.linkedin.deco.recipe.anonymous.Anon2115336743"}}},"state":{"type":"string"},"universalName":{"type":"string"},"groupUrn":{"type":"string"},"localizedDescription":{"type":"string"},"localizedWebsite":{"type":"string"},"customizableCallToActionUnion":{"type":{"union":{"organizationProductLeadGenFormCallToAction":"com.linkedin.deco.recipe.anonymous.Anon792975169","organizationProductCallToAction":"com.linkedin.deco.recipe.anonymous.Anon625674184","organizationProductAddSkillCallToAction":"com.linkedin.deco.recipe.anonymous.Anon2115336743"}}},"group":{"type":"com.linkedin.deco.recipe.anonymous.Anon280473862","resolvedFrom":"groupUrn"},"hashtag":{"type":{"map":"com.linkedin.deco.recipe.anonymous.Anon2070591469"},"resolvedFrom":"hashtagUrns"},"localizedName":{"type":"string"},"connectionsUsingProductProfiles":{"type":"com.linkedin.deco.recipe.anonymous.Anon1969742478","isInjection":true},"mediaSections":{"type":{"array":"com.linkedin.deco.recipe.anonymous.Anon805140200"}},"productCategoriesResolutionResults":{"type":{"map":"com.linkedin.voyager.dash.deco.organization.FullProductCategory"},"resolvedFrom":"productCategories"},"hashtagUrns":{"type":{"array":"string"}},"productCategories":{"type":{"array":"string"}},"memberFacingCallToActionUnion":{"type":{"union":{"organizationProductLeadGenFormCallToAction":"com.linkedin.deco.recipe.anonymous.Anon792975169","organizationProductCallToAction":"com.linkedin.deco.recipe.anonymous.Anon625674184","organizationProductAddSkillCallToAction":"com.linkedin.deco.recipe.anonymous.Anon2115336743"}}},"standardizedSkillUrns":{"type":{"array":"string"}},"organizationalPageUrn":{"type":"string"},"autoPublished":{"type":"boolean"},"organizationsUsingProductUrns":{"type":{"array":"string"}},"standardizedSkill":{"type":{"map":"com.linkedin.deco.recipe.anonymous.Anon503562015"},"resolvedFrom":"standardizedSkillUrns"}},"baseType":"com.linkedin.voyager.dash.organization.OrganizationProduct"},"com.linkedin.voyager.dash.deco.launchpad.OrganizationPermissions":{"fields":{"canReadOrganizationVisitorAnalytics":{"type":"boolean"},"canCreateBroadcast":{"type":"boolean"},"canMembersInviteToFollow":{"type":"boolean"},"canSeeOrganizationAdministrativePage":{"type":"boolean"}},"baseType":"com.linkedin.voyager.dash.organization.OrganizationPermissions"},"com.linkedin.deco.recipe.anonymous.Anon1869367056":{"fields":{"entityUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.groups.Group"},"com.linkedin.voyager.dash.deco.identity.profile.ProfileActionsInjection":{"fields":{"secondaryActionResolutionResult":{"type":{"union":{"personalizedConnect":"com.linkedin.deco.recipe.anonymous.Anon4539795","saveToPdf":"com.linkedin.deco.recipe.anonymous.Anon587401631","followingState":"com.linkedin.deco.recipe.anonymous.Anon1760283115","ignore":"com.linkedin.deco.recipe.anonymous.Anon1312950162","composeOption":"com.linkedin.deco.recipe.anonymous.Anon545512017","withdraw":"com.linkedin.deco.recipe.anonymous.Anon1213132949","saveInSalesNavigatorState":"com.linkedin.deco.recipe.anonymous.Anon1975396536"}},"resolvedFrom":"secondaryAction"},"primaryActionResolutionResult":{"type":{"union":{"personalizedConnect":"com.linkedin.deco.recipe.anonymous.Anon4539795","saveToPdf":"com.linkedin.deco.recipe.anonymous.Anon587401631","followingState":"com.linkedin.deco.recipe.anonymous.Anon1760283115","ignore":"com.linkedin.deco.recipe.anonymous.Anon1312950162","composeOption":"com.linkedin.deco.recipe.anonymous.Anon545512017","withdraw":"com.linkedin.deco.recipe.anonymous.Anon1213132949","saveInSalesNavigatorState":"com.linkedin.deco.recipe.anonymous.Anon1975396536"}},"resolvedFrom":"primaryAction"},"trackingIdentifier":{"type":"bytes"},"primaryAction":{"type":{"union":{"personalizedConnect":"string","saveToPdf":"string","shareProfileUrlViaMessage":"string","saveToPdfUrl":"string","composeOption":"string","saveInSalesNavigatorState":"string","statefulAction":"com.linkedin.voyager.dash.deco.common.ux.StatefulButtonModel","viewProfileInExternalContext":"com.linkedin.voyager.dash.deco.identity.profile.ViewProfileInExternalContextAction","statelessAction":"string","followingState":"string","report":"com.linkedin.deco.recipe.anonymous.Anon743120773","ignore":"string","shareProfileUrl":"string","connection":"com.linkedin.voyager.dash.deco.identity.profile.MemberRelationshipWrapper","withdraw":"string"}}},"secondaryAction":{"type":{"union":{"personalizedConnect":"string","saveToPdf":"string","shareProfileUrlViaMessage":"string","saveToPdfUrl":"string","composeOption":"string","saveInSalesNavigatorState":"string","statefulAction":"com.linkedin.voyager.dash.deco.common.ux.StatefulButtonModel","viewProfileInExternalContext":"com.linkedin.voyager.dash.deco.identity.profile.ViewProfileInExternalContextAction","statelessAction":"string","followingState":"string","report":"com.linkedin.deco.recipe.anonymous.Anon743120773","ignore":"string","shareProfileUrl":"string","connection":"com.linkedin.voyager.dash.deco.identity.profile.MemberRelationshipWrapper","withdraw":"string"}}},"overflowActionsResolutionResults":{"type":{"map":{"union":{"personalizedConnect":"com.linkedin.deco.recipe.anonymous.Anon4539795","saveToPdf":"com.linkedin.deco.recipe.anonymous.Anon587401631","followingState":"com.linkedin.deco.recipe.anonymous.Anon1760283115","ignore":"com.linkedin.deco.recipe.anonymous.Anon1312950162","composeOption":"com.linkedin.deco.recipe.anonymous.Anon545512017","withdraw":"com.linkedin.deco.recipe.anonymous.Anon1213132949","saveInSalesNavigatorState":"com.linkedin.deco.recipe.anonymous.Anon1975396536"}}},"resolvedFrom":"overflowActions"},"overflowActions":{"type":{"array":{"union":{"personalizedConnect":"string","saveToPdf":"string","shareProfileUrlViaMessage":"string","saveToPdfUrl":"string","composeOption":"string","saveInSalesNavigatorState":"string","statefulAction":"com.linkedin.voyager.dash.deco.common.ux.StatefulButtonModel","viewProfileInExternalContext":"com.linkedin.voyager.dash.deco.identity.profile.ViewProfileInExternalContextAction","statelessAction":"string","followingState":"string","report":"com.linkedin.deco.recipe.anonymous.Anon743120773","ignore":"string","shareProfileUrl":"string","connection":"com.linkedin.voyager.dash.deco.identity.profile.MemberRelationshipWrapper","withdraw":"string"}}}},"trackingId":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.identity.profile.actions.ProfileActions"},"com.linkedin.deco.recipe.anonymous.Anon2127563472":{"fields":{"followerCount":{"type":"long"},"entityUrn":{"type":"string"},"preDashFollowingInfoUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.feed.FollowingState"},"com.linkedin.deco.recipe.anonymous.Anon280473862":{"fields":{"viewerGroupMembership":{"type":"com.linkedin.deco.recipe.anonymous.Anon632521550","resolvedFrom":"viewerGroupMembershipUrn"},"displayNotificationSubscriptionLevelOptions":{"type":"boolean"},"groupPostNotificationsEdgeSetting":{"type":"com.linkedin.deco.recipe.anonymous.Anon735489647","resolvedFrom":"groupPostNotificationsEdgeSettingUrn"},"groupPostNotificationsEdgeSettingUrn":{"type":"string"},"postApprovalEnabled":{"type":"boolean"},"backendGroupUrn":{"type":"string"},"memberCount":{"type":"int"},"owners":{"type":"com.linkedin.deco.recipe.anonymous.Anon1299693827","isInjection":true},"memberConnectionsFacePile":{"type":"com.linkedin.voyager.dash.deco.common.image.ImageViewModel"},"memberConnections":{"type":"com.linkedin.deco.recipe.anonymous.Anon721197842","isInjection":true},"membersFacePile":{"type":"com.linkedin.voyager.dash.deco.common.image.ImageViewModel"},"directJoinEnabled":{"type":"boolean"},"entityUrn":{"type":"string"},"logo":{"type":{"union":{"url":"string","vectorImage":"com.linkedin.voyager.dash.deco.common.VectorImage"}}},"globalNewPostNotificationSettingOn":{"type":"boolean"},"viewerGroupMembershipUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.groups.Group"},"com.linkedin.deco.recipe.anonymous.Anon514683669":{"fields":{"currentProgress":{"type":"int"},"threshold":{"type":"int"},"progressText":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.launchpad.LaunchpadProgressMeter"},"com.linkedin.voyager.dash.deco.common.sponsored.SponsoredUrlAttributes":{"fields":{"impressionId":{"type":"string"},"unwrappedUrlDomain":{"type":"string"},"creativeId":{"type":"string"},"campaignId":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.common.sponsored.SponsoredUrlAttributes"},"com.linkedin.deco.recipe.anonymous.Anon2036460800":{"fields":{"insightImage":{"type":"com.linkedin.voyager.dash.deco.common.image.ImageViewModel"},"sharedConnectionDetailTarget":{"type":"string"},"text":{"type":"com.linkedin.voyager.dash.deco.common.text.TextViewModelV2"},"navigationUrl":{"type":"string"},"entityUrn":{"type":"string"},"sharedConnectionDetailTargetResolutionResult":{"type":"com.linkedin.deco.recipe.anonymous.Anon587401631","resolvedFrom":"sharedConnectionDetailTarget"}},"baseType":"com.linkedin.voyager.dash.relationships.Insight"},"com.linkedin.voyager.dash.deco.relationships.MemberRelationshipV2ForInjection":{"fields":{"memberRelationshipData":{"type":{"union":{"noInvitation":"com.linkedin.deco.recipe.anonymous.Anon1031101697","invitation":"com.linkedin.voyager.dash.deco.relationships.Invitation","connection":"com.linkedin.voyager.dash.deco.relationships.Connection"}}},"entityUrn":{"type":"string"},"memberRelationshipUnion":{"type":{"union":{"self":"com.linkedin.restli.common.EmptyRecord","connection":"com.linkedin.voyager.dash.deco.relationships.Connection","noConnection":"com.linkedin.voyager.dash.deco.relationships.NoConnection"}}}},"baseType":"com.linkedin.voyager.dash.relationships.MemberRelationship"},"com.linkedin.voyager.dash.deco.organization.FullProductCategory":{"fields":{"name":{"type":"com.linkedin.voyager.dash.deco.common.text.TextViewModelV2"},"entityUrn":{"type":"string"},"productCategoryPageUrl":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.organization.ProductCategory"},"com.linkedin.deco.recipe.anonymous.Anon1428941918":{"fields":{"paging":{"type":"com.linkedin.voyager.dash.deco.common.FullPaging"},"elements":{"type":{"array":"com.linkedin.deco.recipe.anonymous.Anon2116040434"}}},"baseType":"com.linkedin.restli.common.CollectionResponse"},"com.linkedin.deco.recipe.anonymous.Anon4539795":{"fields":{"entityUrn":{"type":"string"},"memberRelationshipUnion":{"type":{"union":{"self":"com.linkedin.restli.common.EmptyRecord","connection":"com.linkedin.deco.recipe.anonymous.Anon2134644859","noConnection":"com.linkedin.deco.recipe.anonymous.Anon2058972220"}}}},"baseType":"com.linkedin.voyager.dash.relationships.MemberRelationship"},"com.linkedin.voyager.dash.deco.common.text.ProfileForMention":{"fields":{"entityUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.identity.profile.Profile"},"com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrlAndAttribution":{"fields":{"attribution":{"type":"string"},"rootUrl":{"type":"string"},"artifacts":{"type":{"array":"com.linkedin.voyager.dash.deco.common.VectorArtifact"}}},"baseType":"com.linkedin.common.VectorImage"},"com.linkedin.deco.recipe.anonymous.Anon831664802":{"fields":{"entityUrn":{"type":"string"},"invitationId":{"type":"long"}},"baseType":"com.linkedin.voyager.dash.relationships.invitation.Invitation"},"com.linkedin.deco.recipe.anonymous.Anon2070591469":{"fields":{"actionTarget":{"type":"string"},"entityUrn":{"type":"string"},"followingState":{"type":"com.linkedin.deco.recipe.anonymous.Anon2127563472","isInjection":true},"displayName":{"type":"string"},"trackingUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.feed.Hashtag"},"com.linkedin.voyager.dash.deco.common.Industry":{"fields":{"name":{"type":"string"},"entityUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.common.Industry"},"com.linkedin.deco.recipe.anonymous.Anon912817537":{"fields":{"memberDistance":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.relationships.NoConnection"},"com.linkedin.deco.recipe.anonymous.Anon1154789573":{"fields":{"maxResponseLength":{"type":"int"},"response":{"type":"string"},"validationType":{"type":"string"},"minResponseLength":{"type":"int"}},"baseType":"com.linkedin.voyager.dash.sponsoredcontent.leadgen.TextInputComponent"},"com.linkedin.deco.recipe.anonymous.Anon8381687":{"fields":{"multipleChoiceQuestionOptions":{"type":{"array":"com.linkedin.deco.recipe.anonymous.Anon1507465610"}},"placeholderText":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.sponsoredcontent.leadgen.DropdownSelectComponent"},"com.linkedin.voyager.dash.deco.relationships.InvitationRaw":{"fields":{"genericInvitationType":{"type":"string"},"invitationId":{"type":"long"},"sharedSecret":{"type":"string"},"entityUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.relationships.invitation.Invitation"},"com.linkedin.voyager.dash.deco.common.video.AdaptiveStream":{"fields":{"initialBitRate":{"type":"int"},"protocol":{"type":"string"},"mediaType":{"type":"string"},"masterPlaylists":{"type":{"array":"com.linkedin.voyager.dash.deco.common.video.StreamingLocation"}}},"baseType":"com.linkedin.videocontent.AdaptiveStream"},"com.linkedin.deco.recipe.anonymous.Anon1529112441":{"fields":{"originalImageUrl":{"type":"string"},"originalHeight":{"type":"int"},"url":{"type":"string"},"originalWidth":{"type":"int"}},"baseType":"com.linkedin.voyager.dash.common.ImageUrl"},"com.linkedin.voyager.dash.deco.common.video.StreamingLocation":{"fields":{"url":{"type":"string"},"expiresAt":{"type":"long"}},"baseType":"com.linkedin.videocontent.StreamingLocation"},"com.linkedin.voyager.dash.deco.launchpad.LaunchpadView":{"fields":{"launchpadCards":{"type":{"array":"com.linkedin.deco.recipe.anonymous.Anon903390836"}},"dismissDialog":{"type":"com.linkedin.deco.recipe.anonymous.Anon1670704461"},"headerImage":{"type":"com.linkedin.voyager.dash.deco.common.image.ImageViewModel"},"focusedCardIndex":{"type":"int"},"progressMeter":{"type":"com.linkedin.deco.recipe.anonymous.Anon514683669"},"branding":{"type":"com.linkedin.deco.recipe.anonymous.Anon1647280845"},"dismissible":{"type":"boolean"},"pageKey":{"type":"com.linkedin.voyager.dash.deco.launchpad.PageKey"},"theme":{"type":"string"},"legoTrackingToken":{"type":"string"},"title":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.launchpad.LaunchpadView"},"com.linkedin.voyager.dash.deco.common.video.VideoPlayMetadata":{"fields":{"thumbnail":{"type":"com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrl"},"progressiveStreams":{"type":{"array":"com.linkedin.voyager.dash.deco.common.video.ProgressiveDownloadMetadata"}},"liveStreamCreatedAt":{"type":"long"},"prevMedia":{"type":"string"},"transcripts":{"type":{"array":"com.linkedin.voyager.dash.deco.common.video.Transcript"}},"aspectRatio":{"type":"float"},"media":{"type":"string"},"adaptiveStreams":{"type":{"array":"com.linkedin.voyager.dash.deco.common.video.AdaptiveStream"}},"liveStreamEndedAt":{"type":"long"},"duration":{"type":"long"},"provider":{"type":"string"},"entityUrn":{"type":"string"},"nextMedia":{"type":"string"},"thumbnails":{"type":{"array":"com.linkedin.voyager.dash.deco.common.video.Thumbnail"}},"trackingId":{"type":"string"}},"baseType":"com.linkedin.videocontent.VideoPlayMetadata"},"com.linkedin.voyager.dash.deco.identity.profile.ProfilePhotoDecoSpecReadOnlyBackground":{"fields":{"displayImageUrn":{"type":"string"},"displayImageReference":{"type":{"union":{"url":"string","vectorImage":"com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrlAndAttribution"}}}},"baseType":"com.linkedin.voyager.dash.identity.profile.PhotoFilterPicture"},"com.linkedin.deco.recipe.anonymous.Anon2058972220":{"fields":{"invitationUnion":{"type":{"union":{"noInvitation":"com.linkedin.deco.recipe.anonymous.Anon412783727","invitation":"com.linkedin.deco.recipe.anonymous.Anon831664802"}}}},"baseType":"com.linkedin.voyager.dash.relationships.NoConnection"},"com.linkedin.deco.recipe.anonymous.Anon1150537667":{"fields":{"requiredFieldMissingErrorText":{"type":"string"},"formComponentUnion":{"type":{"union":{"textFieldComponent":"com.linkedin.deco.recipe.anonymous.Anon1358424483","dropdownSelectComponent":"com.linkedin.deco.recipe.anonymous.Anon8381687","textInputComponent":"com.linkedin.deco.recipe.anonymous.Anon1154789573","checkboxComponent":"com.linkedin.deco.recipe.anonymous.Anon879961581"}}},"question":{"type":"com.linkedin.voyager.dash.deco.common.text.TextViewModelV2"},"required":{"type":"boolean"},"editable":{"type":"boolean"},"leadGenFormQuestionUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.sponsoredcontent.leadgen.LeadGenFormQuestion"},"com.linkedin.voyager.dash.deco.relationships.Invitation":{"fields":{"inviteeMemberResolutionResult":{"type":"com.linkedin.deco.recipe.anonymous.Anon336652209","resolvedFrom":"inviteeMember"},"invitationType":{"type":"string"},"inviteeMember":{"type":"string"},"entityUrn":{"type":"string"},"invitationState":{"type":"string"},"invitationId":{"type":"long"},"sharedSecret":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.relationships.invitation.Invitation"},"com.linkedin.voyager.dash.deco.common.IndustryV2":{"fields":{"name":{"type":"string"},"entityUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.identity.profile.IndustryV2"},"com.linkedin.voyager.dash.deco.launchpad.ProfileTopCardForEntityFollow":{"fields":{"lastName":{"type":"string"},"profileTopEducation":{"type":"com.linkedin.deco.recipe.anonymous.Anon964860152","isInjection":true},"profilePositions":{"type":"com.linkedin.deco.recipe.anonymous.Anon1861880920","isInjection":true},"educationOnProfileTopCardShown":{"type":"boolean"},"profileTopPosition":{"type":"com.linkedin.deco.recipe.anonymous.Anon1449981882","isInjection":true},"associatedHashtagsCopy":{"type":"com.linkedin.voyager.dash.deco.common.text.TextViewModelV2"},"profilePicture":{"type":"com.linkedin.voyager.dash.deco.identity.profile.ProfilePhotoDecoSpecReadOnlyProfilePicture"},"firstName":{"type":"string"},"profileInsight":{"type":"com.linkedin.deco.recipe.anonymous.Anon361088429","isInjection":true},"geoLocation":{"type":"com.linkedin.deco.recipe.anonymous.Anon708807917"},"entityUrn":{"type":"string"},"followingState":{"type":"com.linkedin.deco.recipe.anonymous.Anon89639392","isInjection":true},"memberRelationship":{"type":"com.linkedin.voyager.dash.deco.relationships.MemberRelationshipV2ForInjection","isInjection":true},"companyNameOnProfileTopCardShown":{"type":"boolean"},"headline":{"type":"string"},"publicIdentifier":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.identity.profile.Profile"},"com.linkedin.deco.recipe.anonymous.Anon1069349607":{"fields":{"entityUrn":{"type":"string"},"memberRelationshipUnion":{"type":{"union":{"self":"com.linkedin.restli.common.EmptyRecord","connection":"com.linkedin.deco.recipe.anonymous.Anon2134644859","noConnection":"com.linkedin.deco.recipe.anonymous.Anon912817537"}}}},"baseType":"com.linkedin.voyager.dash.relationships.MemberRelationship"},"com.linkedin.deco.recipe.anonymous.Anon1128782547":{"fields":{"entityUrn":{"type":"string"},"joinedAt":{"type":"long"},"profile":{"type":"com.linkedin.deco.recipe.anonymous.Anon437558093","resolvedFrom":"profileUrn"},"groupUrn":{"type":"string"},"preDashEntityUrn":{"type":"string"},"profileUrn":{"type":"string"},"status":{"type":"string"},"group":{"type":"com.linkedin.deco.recipe.anonymous.Anon1869367056","resolvedFrom":"groupUrn"}},"baseType":"com.linkedin.voyager.dash.groups.GroupMembership"},"com.linkedin.deco.recipe.anonymous.Anon1509374374":{"fields":{"displayText":{"type":"string"},"url":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.organization.GenericCallToAction"},"com.linkedin.deco.recipe.anonymous.Anon503562015":{"fields":{"name":{"type":"string"},"entityUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.jobs.StandardizedSkill"},"com.linkedin.deco.recipe.anonymous.Anon743011996":{"fields":{"productCategories":{"type":{"array":"string"}},"signatureProduct":{"type":"boolean"},"localizedName":{"type":"string"},"organizationsUsingProduct":{"type":{"map":"com.linkedin.deco.recipe.anonymous.Anon570745354"},"resolvedFrom":"organizationsUsingProductUrns"},"entityUrn":{"type":"string"},"logo":{"type":"com.linkedin.voyager.dash.deco.common.image.ImageViewModel"},"connectionsUsingProductProfiles":{"type":"com.linkedin.deco.recipe.anonymous.Anon1122581856","isInjection":true},"company":{"type":"com.linkedin.deco.recipe.anonymous.Anon1927941263","resolvedFrom":"companyUrn"},"universalName":{"type":"string"},"organizationsUsingProductUrns":{"type":{"array":"string"}},"productCategoriesResolutionResults":{"type":{"map":"com.linkedin.voyager.dash.deco.organization.FullProductCategory"},"resolvedFrom":"productCategories"},"companyUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.organization.OrganizationProduct"},"com.linkedin.deco.recipe.anonymous.Anon903390836":{"fields":{"backgroundImage":{"type":"com.linkedin.voyager.dash.deco.common.image.ImageViewModel"},"cardType":{"type":"string"},"icon":{"type":"com.linkedin.voyager.dash.deco.common.image.ImageViewModel"},"pageKey":{"type":"com.linkedin.voyager.dash.deco.launchpad.PageKey"},"completed":{"type":"boolean"},"legoTrackingToken":{"type":"string"},"cardTitle":{"type":"com.linkedin.voyager.dash.deco.common.text.TextViewModelV2"},"ctas":{"type":{"array":"com.linkedin.deco.recipe.anonymous.Anon1684919054"}},"animate":{"type":"boolean"},"videoMetadata":{"type":"com.linkedin.voyager.dash.deco.common.video.VideoPlayMetadata"},"cardLabel":{"type":"com.linkedin.voyager.dash.deco.common.text.TextViewModelV2"},"attributeUnion":{"type":{"union":{"followOrganization":"string","launchpad":"string","jobSearchQuery":"com.linkedin.voyager.dash.deco.launchpad.JobSearchQuery","companyJYMBII":"string","generalJYMBII":{"array":"string"},"connectWithEntity":"string","viewExperienceEntity":"string","entityActivityFeed":"string","followPostCreator":"string","edgeBuilding":{"array":"com.linkedin.voyager.dash.deco.launchpad.EdgeBuildingCohortReason"},"jobAlertJYMBII":{"array":"string"},"organizationActivityFeed":"string"}}},"insightImage":{"type":"com.linkedin.voyager.dash.deco.common.image.ImageViewModel"},"overlayImage":{"type":"com.linkedin.voyager.dash.deco.common.image.ImageViewModel"},"attribute":{"type":{"union":{"followOrganization":"com.linkedin.voyager.dash.deco.launchpad.OrganizationTopCardForEntityFollow","companyJYMBII":"com.linkedin.deco.recipe.anonymous.Anon184130218","generalJYMBII":{"map":"com.linkedin.deco.recipe.anonymous.Anon1042323916"},"connectWithEntity":"com.linkedin.voyager.dash.deco.launchpad.ProfileTopCardForEntityFollow","viewExperienceEntity":"com.linkedin.voyager.dash.deco.launchpad.ProfileTopCardForEntityFollow","entityActivityFeed":"com.linkedin.deco.recipe.anonymous.Anon587401631","followPostCreator":"com.linkedin.voyager.dash.deco.launchpad.ProfileTopCardForEntityFollow","jobAlertJYMBII":{"map":"com.linkedin.deco.recipe.anonymous.Anon1042323916"},"organizationActivityFeed":"com.linkedin.deco.recipe.anonymous.Anon1927941263"}},"resolvedFrom":"attributeUnion"},"cardSubtitle":{"type":"com.linkedin.voyager.dash.deco.common.text.TextViewModelV2"},"cardStyle":{"type":"string"},"entitySize":{"type":"int"}},"baseType":"com.linkedin.voyager.dash.launchpad.LaunchpadCard"},"com.linkedin.deco.recipe.anonymous.Anon708807917":{"fields":{"geo":{"type":"com.linkedin.deco.recipe.anonymous.Anon1444411496","resolvedFrom":"geoUrn"},"geoUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.identity.profile.ProfileGeoLocation"},"com.linkedin.voyager.dash.deco.identity.profile.ProfilePhotoDecoSpecReadOnlyProfilePicture":{"fields":{"displayImageWithFrameReferenceUnion":{"type":{"union":{"url":"string","vectorImage":"com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrlAndAttribution"}}},"frameType":{"type":"string"},"a11yText":{"type":"string"},"displayImageUrn":{"type":"string"},"displayImageReference":{"type":{"union":{"url":"string","vectorImage":"com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrlAndAttribution"}}}},"baseType":"com.linkedin.voyager.dash.identity.profile.PhotoFilterPicture"},"com.linkedin.deco.recipe.anonymous.Anon1684919054":{"fields":{"ctaColor":{"type":"string"},"ctaType":{"type":"string"},"ctaStyle":{"type":"string"},"presentationStyle":{"type":"string"},"shareMessage":{"type":"com.linkedin.voyager.dash.deco.common.text.TextViewModelV2"},"ctaTitle":{"type":"com.linkedin.voyager.dash.deco.common.text.TextViewModelV2"},"deeplinkUrl":{"type":"string"},"legoActionCategory":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.launchpad.LaunchpadCta"},"com.linkedin.deco.recipe.anonymous.Anon858976209":{"fields":{"type":{"type":"string"},"epochAt":{"type":"long"}},"baseType":"com.linkedin.voyager.dash.common.text.EpochTime"},"com.linkedin.voyager.dash.deco.identity.profile.ViewProfileInExternalContextAction":{"fields":{"deeplinkUrl":{"type":"string"},"recruiterContext":{"type":"boolean"}},"baseType":"com.linkedin.voyager.dash.identity.profile.actions.ViewProfileInExternalContextAction"},"com.linkedin.deco.recipe.anonymous.Anon1843097075":{"fields":{"invitationUnion":{"type":{"union":{"noInvitation":"com.linkedin.deco.recipe.anonymous.Anon881636240","invitation":"com.linkedin.deco.recipe.anonymous.Anon1286825962"}}}},"baseType":"com.linkedin.voyager.dash.relationships.NoConnection"},"com.linkedin.deco.recipe.anonymous.Anon89639392":{"fields":{"followerCount":{"type":"long"},"entityUrn":{"type":"string"},"preDashFollowingInfoUrn":{"type":"string"},"following":{"type":"boolean"}},"baseType":"com.linkedin.voyager.dash.feed.FollowingState"},"com.linkedin.deco.recipe.anonymous.Anon655007389":{"fields":{"name":{"type":"com.linkedin.voyager.dash.deco.common.text.TextViewModelV2"},"imageUnion":{"type":{"union":{"url":"string","vectorImage":"com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrlAndAttribution"}}}},"baseType":"com.linkedin.voyager.dash.common.media.StickerLinkSmallTemplateView"},"com.linkedin.voyager.dash.deco.common.video.TranscriptLine":{"fields":{"lineStartAt":{"type":"long"},"caption":{"type":"string"},"lineEndAt":{"type":"long"}},"baseType":"com.linkedin.videocontent.TranscriptLine"},"com.linkedin.voyager.dash.deco.launchpad.CallToAction":{"fields":{"displayText":{"type":"string"},"visible":{"type":"boolean"},"type":{"type":"string"},"url":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.organization.CallToAction"},"com.linkedin.deco.recipe.anonymous.Anon1283481334":{"fields":{"profilePicture":{"type":"com.linkedin.voyager.dash.deco.identity.profile.ProfilePhotoDecoSpecReadOnlyProfilePicture"},"lastName":{"type":"string"},"firstName":{"type":"string"},"profileProfileActions":{"type":"com.linkedin.voyager.dash.deco.identity.profile.ProfileActionsInjection","isInjection":true},"entityUrn":{"type":"string"},"memberRelationship":{"type":"com.linkedin.voyager.dash.deco.relationships.MemberRelationshipV2ForInjection","isInjection":true},"publicIdentifier":{"type":"string"},"headline":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.identity.profile.Profile"},"com.linkedin.deco.recipe.anonymous.Anon625674184":{"fields":{"type":{"type":"string"},"callToAction":{"type":"com.linkedin.deco.recipe.anonymous.Anon1509374374"}},"baseType":"com.linkedin.voyager.dash.organization.OrganizationProductCallToAction"},"com.linkedin.voyager.dash.deco.common.text.OrganizationalPage":{"fields":{"entityUrn":{"type":"string"},"localizedName":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.organization.OrganizationalPage"},"com.linkedin.deco.recipe.anonymous.Anon1031101697":{"fields":{"targetInviteeResolutionResult":{"type":"com.linkedin.voyager.dash.deco.relationships.ProfileWithEmailRequired","resolvedFrom":"targetInvitee"},"inviter":{"type":"string"},"targetInvitee":{"type":"string"},"invitationRelationshipForm":{"type":"com.linkedin.deco.recipe.anonymous.Anon918376989"},"inviterResolutionResult":{"type":"com.linkedin.voyager.dash.deco.relationships.ProfileWithIweWarned","resolvedFrom":"inviter"}},"baseType":"com.linkedin.voyager.dash.relationships.invitation.NoInvitation"},"com.linkedin.deco.recipe.anonymous.Anon1271139837":{"fields":{"entityUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.common.Geo"},"com.linkedin.deco.recipe.anonymous.Anon163061530":{"fields":{"name":{"type":"string"},"entityUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.groups.Group"},"com.linkedin.voyager.dash.deco.relationships.profile":{"fields":{"lastName":{"type":"string"},"firstName":{"type":"string"},"creator":{"type":"boolean"},"entityUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.identity.profile.Profile"},"com.linkedin.voyager.dash.deco.common.text.ProfileForFullName":{"fields":{"lastName":{"type":"string"},"firstName":{"type":"string"},"entityUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.identity.profile.Profile"},"com.linkedin.deco.recipe.anonymous.Anon378816379":{"fields":{"viewer":{"type":"com.linkedin.deco.recipe.anonymous.Anon430310092","resolvedFrom":"viewerUrn"},"company":{"type":"com.linkedin.deco.recipe.anonymous.Anon660720507","resolvedFrom":"companyUrn"},"companyUrn":{"type":"string"},"viewerUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.relationships.MemberToCompanyFollowMetadata"},"com.linkedin.deco.recipe.anonymous.Anon743120773":{"fields":{"authorProfileId":{"type":"string"},"targetUrn":{"type":"string"},"contentSource":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.common.semaphore.SemaphoreContext"},"com.linkedin.deco.recipe.anonymous.Anon805140200":{"fields":{"mediaContentUnion":{"type":{"union":{"embeddedVideo":"com.linkedin.voyager.dash.deco.organization.EmbeddedVideoDecoSpec","url":"string","videoPlayMetadata":"com.linkedin.voyager.dash.deco.common.video.VideoPlayMetadata","vectorImage":"com.linkedin.voyager.dash.deco.common.VectorImage"}}},"description":{"type":"string"},"mediaEntityUnion":{"type":{"union":{"digitalMediaAssetUrn":"string","articleUrn":"string"}}},"title":{"type":"string"},"mediaSource":{"type":"string"},"primary":{"type":"boolean"}},"baseType":"com.linkedin.voyager.dash.organization.MediaSection"},"com.linkedin.deco.recipe.anonymous.Anon964860152":{"fields":{"paging":{"type":"com.linkedin.voyager.dash.deco.common.FullPaging"},"elements":{"type":{"array":"com.linkedin.deco.recipe.anonymous.Anon487759616"}}},"baseType":"com.linkedin.restli.common.CollectionResponse"},"com.linkedin.voyager.dash.deco.relationships.NoConnection":{"fields":{"memberDistance":{"type":"string"},"invitationUnion":{"type":{"union":{"noInvitation":"com.linkedin.deco.recipe.anonymous.Anon1031101697","invitation":"com.linkedin.voyager.dash.deco.relationships.Invitation"}}}},"baseType":"com.linkedin.voyager.dash.relationships.NoConnection"},"com.linkedin.deco.recipe.anonymous.Anon40184024":{"fields":{"ctaText":{"type":"string"},"landingPage":{"type":"com.linkedin.deco.recipe.anonymous.Anon1586568086"},"document":{"type":"com.linkedin.deco.recipe.anonymous.Anon856218111"},"confirmationTitle":{"type":"com.linkedin.voyager.dash.deco.common.text.TextViewModelV2"},"urlViewingBehavior":{"type":"string"},"sponsoredUrlAttributes":{"type":"com.linkedin.voyager.dash.deco.common.sponsored.SponsoredUrlAttributes"},"confirmationDescription":{"type":"com.linkedin.voyager.dash.deco.common.text.TextViewModelV2"}},"baseType":"com.linkedin.voyager.dash.sponsoredcontent.leadgen.LeadGenGatedContent"},"com.linkedin.deco.recipe.anonymous.Anon40833127":{"fields":{"metadataUnion":{"type":{"union":{"memberToContentSeriesSubscribe":"com.linkedin.deco.recipe.anonymous.Anon489758292"}}},"subscribeActionUrn":{"type":"string"},"subscribeAction":{"type":"com.linkedin.voyager.dash.deco.feed.publishing.SubscribeAction","resolvedFrom":"subscribeActionUrn"}},"baseType":"com.linkedin.voyager.dash.relationships.SubscribeRelationship"},"com.linkedin.deco.recipe.anonymous.Anon2115336743":{"fields":{"displayText":{"type":"string"},"toggledDisplayText":{"type":"string"},"enabled":{"type":"boolean"}},"baseType":"com.linkedin.voyager.dash.organization.OrganizationProductAddSkillCallToAction"},"com.linkedin.deco.recipe.anonymous.Anon336652209":{"fields":{"profilePicture":{"type":"com.linkedin.voyager.dash.deco.identity.profile.ProfilePhotoDecoSpecReadOnlyProfilePicture"},"memorialized":{"type":"boolean"},"lastName":{"type":"string"},"firstName":{"type":"string"},"tempStatus":{"type":"string"},"entityUrn":{"type":"string"},"tempStatusEmoji":{"type":"string"},"publicIdentifier":{"type":"string"},"headline":{"type":"string"},"tempStatusExpiredAtUnion":{"type":{"union":{"customizedExpiredAt":"long","standardizedExpiration":"string"}}}},"baseType":"com.linkedin.voyager.dash.identity.profile.Profile"},"com.linkedin.voyager.dash.deco.common.VectorArtifact":{"fields":{"width":{"type":"int"},"fileIdentifyingUrlPathSegment":{"type":"string"},"expiresAt":{"type":"long"},"height":{"type":"int"}},"baseType":"com.linkedin.common.VectorArtifact"},"com.linkedin.voyager.dash.deco.common.text.School":{"fields":{"name":{"type":"string"},"entityUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.organization.School"},"com.linkedin.deco.recipe.anonymous.Anon2066892616":{"fields":{"invitationType":{"type":"string"},"invitationId":{"type":"long"},"sharedSecret":{"type":"string"},"entityUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.relationships.invitation.Invitation"},"com.linkedin.voyager.dash.deco.launchpad.PageKey":{"fields":{"pageKey":{"type":"string"},"anchorPage":{"type":"boolean"}},"baseType":"com.linkedin.voyager.dash.common.tracking.PageKey"},"com.linkedin.deco.recipe.anonymous.Anon430310092":{"fields":{"entityUrn":{"type":"string"},"creator":{"type":"boolean"}},"baseType":"com.linkedin.voyager.dash.identity.profile.Profile"},"com.linkedin.deco.recipe.anonymous.Anon1586568086":{"fields":{"url":{"type":"string"},"text":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.common.Link"},"com.linkedin.deco.recipe.anonymous.Anon1976702492":{"fields":{"iweWarned":{"type":"boolean"},"entityUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.identity.profile.Profile"},"com.linkedin.deco.recipe.anonymous.Anon437558093":{"fields":{"profilePicture":{"type":"com.linkedin.voyager.dash.deco.identity.profile.ProfilePhotoDecoSpecReadOnlyProfilePicture"},"memorialized":{"type":"boolean"},"lastName":{"type":"string"},"firstName":{"type":"string"},"tempStatus":{"type":"string"},"entityUrn":{"type":"string"},"memberRelationship":{"type":"com.linkedin.deco.recipe.anonymous.Anon1069349607","isInjection":true},"tempStatusEmoji":{"type":"string"},"publicIdentifier":{"type":"string"},"headline":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.identity.profile.Profile"},"com.linkedin.deco.recipe.anonymous.Anon1507465610":{"fields":{"type":{"type":"string"},"textOption":{"type":"string"},"selected":{"type":"boolean"}},"baseType":"com.linkedin.voyager.dash.sponsoredcontent.leadgen.MultipleChoiceQuestionOptions"},"com.linkedin.deco.recipe.anonymous.Anon409680083":{"fields":{"type":{"type":"string"},"index":{"type":"int"}},"baseType":"com.linkedin.voyager.dash.common.text.ListItemStyle"},"com.linkedin.deco.recipe.anonymous.Anon1792705474":{"fields":{"invitationUnion":{"type":{"union":{"noInvitation":"com.linkedin.deco.recipe.anonymous.Anon881636240","invitation":"com.linkedin.deco.recipe.anonymous.Anon2066892616"}}}},"baseType":"com.linkedin.voyager.dash.relationships.NoConnection"},"com.linkedin.deco.recipe.anonymous.Anon1369245809":{"fields":{"name":{"type":"string"},"entityUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.identity.profile.StandardizedTitle"},"com.linkedin.deco.recipe.anonymous.Anon412783727":{"fields":{"targetInviteeResolutionResult":{"type":"com.linkedin.deco.recipe.anonymous.Anon352881287","resolvedFrom":"targetInvitee"},"inviter":{"type":"string"},"targetInvitee":{"type":"string"},"inviterResolutionResult":{"type":"com.linkedin.deco.recipe.anonymous.Anon1976702492","resolvedFrom":"inviter"}},"baseType":"com.linkedin.voyager.dash.relationships.invitation.NoInvitation"},"com.linkedin.deco.recipe.anonymous.Anon918376989":{"fields":{"title":{"type":"string"},"invitationRelationshipOptions":{"type":{"array":"com.linkedin.deco.recipe.anonymous.Anon934606613"}},"subtitle":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.relationships.invitation.InvitationRelationshipForm"},"com.linkedin.voyager.dash.deco.common.Locale":{"fields":{"variant":{"type":"string"},"country":{"type":"string"},"language":{"type":"string"}},"baseType":"com.linkedin.common.Locale"},"com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrl":{"fields":{"rootUrl":{"type":"string"},"artifacts":{"type":{"array":"com.linkedin.voyager.dash.deco.common.VectorArtifact"}}},"baseType":"com.linkedin.common.VectorImage"},"com.linkedin.voyager.dash.deco.common.video.Resolution":{"fields":{"width":{"type":"int"},"height":{"type":"int"}},"baseType":"com.linkedin.videocontent.Resolution"},"com.linkedin.deco.recipe.anonymous.Anon853977300":{"fields":{"entityUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.relationships.Insight"},"com.linkedin.voyager.dash.deco.common.text.ProfileForFamiliarName":{"fields":{"lastName":{"type":"string"},"firstName":{"type":"string"},"entityUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.identity.profile.Profile"},"com.linkedin.deco.recipe.anonymous.Anon579987817":{"fields":{"industryV2Taxonomy":{"type":{"map":"com.linkedin.voyager.dash.deco.common.IndustryV2"},"resolvedFrom":"industryV2TaxonomyUrns"},"industry":{"type":{"map":"com.linkedin.voyager.dash.deco.common.Industry"},"resolvedFrom":"industryUrns"},"industryV2Urns":{"type":{"array":"string"}},"industryUrns":{"type":{"array":"string"}},"url":{"type":"string"},"relevanceReason":{"type":"com.linkedin.voyager.dash.deco.common.ux.baseInsightViewModel"},"industryV2":{"type":{"map":"com.linkedin.voyager.dash.deco.common.Industry"},"resolvedFrom":"industryV2Urns"},"industryV2TaxonomyUrns":{"type":{"array":"string"}},"followingStateUrn":{"type":"string"},"entityUrn":{"type":"string"},"followingState":{"type":"com.linkedin.voyager.dash.deco.feed.FollowingState","resolvedFrom":"followingStateUrn"},"name":{"type":"string"},"logo":{"type":{"union":{"url":"string","vectorImage":"com.linkedin.voyager.dash.deco.common.VectorImage"}}},"universalName":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.organization.Company"},"com.linkedin.voyager.dash.deco.organization.Profile":{"fields":{"profilePicture":{"type":"com.linkedin.voyager.dash.deco.identity.profile.ProfilePhotoDecoSpecReadOnlyProfilePicture"},"lastName":{"type":"string"},"firstName":{"type":"string"},"publicIdentifier":{"type":"string"},"headline":{"type":"string"},"entityUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.identity.profile.Profile"},"com.linkedin.deco.recipe.anonymous.Anon1525160909":{"fields":{"width":{"type":"int"},"imageUrls":{"type":{"array":"string"}},"height":{"type":"int"}},"baseType":"com.linkedin.documentcontent.DocumentResolutionPages"},"com.linkedin.voyager.dash.deco.common.Link":{"fields":{"type":{"type":"string"},"rel":{"type":"string"},"href":{"type":"string"}},"baseType":"com.linkedin.restli.common.Link"},"com.linkedin.voyager.dash.deco.common.ux.baseInsightViewModel":{"fields":{"image":{"type":"com.linkedin.voyager.dash.deco.common.image.ImageViewModel"},"text":{"type":"com.linkedin.voyager.dash.deco.common.text.TextViewModelV2"}},"baseType":"com.linkedin.voyager.dash.common.ux.InsightViewModel"},"com.linkedin.voyager.dash.deco.common.image.School":{"fields":{"logo":{"type":{"union":{"url":"string","vectorImage":"com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrlAndAttribution"}}},"entityUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.organization.School"},"com.linkedin.deco.recipe.anonymous.Anon545512017":{"fields":{"icon":{"type":"com.linkedin.voyager.dash.deco.common.image.ImageViewModel"},"composeNavigationContext":{"type":"com.linkedin.deco.recipe.anonymous.Anon199392175"},"displayText":{"type":"com.linkedin.voyager.dash.deco.common.text.TextViewModelV2"},"textStartIcon":{"type":"com.linkedin.voyager.dash.deco.common.image.ImageViewModel"},"composeOptionType":{"type":"string"},"entityUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.messaging.compose.ComposeOption"},"com.linkedin.voyager.dash.deco.common.VectorImage":{"fields":{"attribution":{"type":"string"},"digitalmediaAsset":{"type":"string"},"rootUrl":{"type":"string"},"artifacts":{"type":{"array":"com.linkedin.voyager.dash.deco.common.VectorArtifact"}}},"baseType":"com.linkedin.common.VectorImage"},"com.linkedin.deco.recipe.anonymous.Anon422795650":{"fields":{"viewerPermissions":{"type":"com.linkedin.voyager.dash.deco.organization.OrganizationPermissions"},"industryV2Taxonomy":{"type":{"map":"com.linkedin.voyager.dash.deco.common.IndustryV2"},"resolvedFrom":"industryV2TaxonomyUrns"},"productsAccessible":{"type":"boolean"},"croppedCoverImageUnion":{"type":{"union":{"url":"string","vectorImage":"com.linkedin.voyager.dash.deco.common.VectorImage"}}},"industry":{"type":{"map":"com.linkedin.voyager.dash.deco.common.Industry"},"resolvedFrom":"industryUrns"},"industryV2Urns":{"type":{"array":"string"}},"lcpStaffingOrganization":{"type":"boolean"},"industryUrns":{"type":{"array":"string"}},"url":{"type":"string"},"lcpTreatment":{"type":"boolean"},"industryV2":{"type":{"map":"com.linkedin.voyager.dash.deco.common.Industry"},"resolvedFrom":"industryV2Urns"},"relevantFollowersForViewerAndOrganization":{"type":"com.linkedin.deco.recipe.anonymous.Anon1075923263","isInjection":true},"industryV2TaxonomyUrns":{"type":{"array":"string"}},"followingStateUrn":{"type":"string"},"entityUrn":{"type":"string"},"followingState":{"type":"com.linkedin.voyager.dash.deco.feed.FollowingState","resolvedFrom":"followingStateUrn"},"originalCoverImageUnion":{"type":{"union":{"url":"string","vectorImage":"com.linkedin.voyager.dash.deco.common.VectorImage"}}},"name":{"type":"string"},"lcpCustomer":{"type":"boolean"},"logo":{"type":{"union":{"url":"string","vectorImage":"com.linkedin.voyager.dash.deco.common.VectorImage"}}},"universalName":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.organization.Company"},"com.linkedin.deco.recipe.anonymous.Anon881636240":{"fields":{"inviter":{"type":"string"},"inviterResolutionResult":{"type":"com.linkedin.deco.recipe.anonymous.Anon587401631","resolvedFrom":"inviter"}},"baseType":"com.linkedin.voyager.dash.relationships.invitation.NoInvitation"},"com.linkedin.voyager.dash.deco.relationships.Connection":{"fields":{"createdAt":{"type":"long"},"connectedMemberResolutionResult":{"type":"com.linkedin.deco.recipe.anonymous.Anon336652209","resolvedFrom":"connectedMember"},"connectedMember":{"type":"string"},"entityUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.relationships.Connection"},"com.linkedin.deco.recipe.anonymous.Anon361088429":{"fields":{"elements":{"type":{"array":"com.linkedin.deco.recipe.anonymous.Anon1447917113"}}},"baseType":"com.linkedin.restli.common.CollectionResponse"},"com.linkedin.voyager.dash.deco.organization.MiniCompany":{"fields":{"name":{"type":"string"},"logo":{"type":{"union":{"url":"string","vectorImage":"com.linkedin.voyager.dash.deco.common.VectorImage"}}},"entityUrn":{"type":"string"},"url":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.organization.Company"},"com.linkedin.deco.recipe.anonymous.Anon198476569":{"fields":{"viewer":{"type":"com.linkedin.deco.recipe.anonymous.Anon430310092","resolvedFrom":"viewerUrn"},"vieweeFollowingViewer":{"type":"boolean"},"viewerUrn":{"type":"string"},"viewee":{"type":"com.linkedin.voyager.dash.deco.relationships.profile","resolvedFrom":"vieweeUrn"},"vieweeUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.relationships.MemberToMemberFollowMetadata"},"com.linkedin.voyager.dash.deco.feed.FollowingState":{"fields":{"followeeCount":{"type":"long"},"entityUrn":{"type":"string"},"trackingUrn":{"type":"string"},"preDashFollowingInfoUrn":{"type":"string"},"following":{"type":"boolean"},"followingType":{"type":"string"},"followerCount":{"type":"long"}},"baseType":"com.linkedin.voyager.dash.feed.FollowingState"},"com.linkedin.deco.recipe.anonymous.Anon1075923263":{"fields":{"paging":{"type":"com.linkedin.voyager.dash.deco.common.FullPaging"},"metadata":{"type":"com.linkedin.deco.recipe.anonymous.Anon523036483"},"elements":{"type":{"array":"com.linkedin.deco.recipe.anonymous.Anon842053443"}}},"baseType":"com.linkedin.restli.common.CollectionResponse"},"com.linkedin.voyager.dash.deco.relationships.DirectionalEntityRelationship":{"fields":{"invitationUrn":{"type":"string"},"entityUrn":{"type":"string"},"invitation":{"type":"com.linkedin.voyager.dash.deco.relationships.InvitationRaw","resolvedFrom":"invitationUrn"},"relationshipDataUnion":{"type":{"union":{"follow":"com.linkedin.deco.recipe.anonymous.Anon191738356","subscribe":"com.linkedin.deco.recipe.anonymous.Anon40833127"}}}},"baseType":"com.linkedin.voyager.dash.relationships.DirectionalEntityRelationship"},"com.linkedin.deco.recipe.anonymous.Anon1568806612":{"fields":{"school":{"type":"com.linkedin.deco.recipe.anonymous.Anon929195650","resolvedFrom":"schoolUrn"},"vectorImage":{"type":"com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrlAndAttribution"},"schoolUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.common.image.NonEntitySchoolLogo"},"com.linkedin.deco.recipe.anonymous.Anon1449981882":{"fields":{"paging":{"type":"com.linkedin.voyager.dash.deco.common.FullPaging"},"elements":{"type":{"array":"com.linkedin.deco.recipe.anonymous.Anon1566936928"}}},"baseType":"com.linkedin.restli.common.CollectionResponse"},"com.linkedin.deco.recipe.anonymous.Anon660720507":{"fields":{"name":{"type":"string"},"entityUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.organization.Company"},"com.linkedin.voyager.dash.deco.relationships.ProfileWithIweWarned":{"fields":{"memorialized":{"type":"boolean"},"lastName":{"type":"string"},"firstName":{"type":"string"},"tempStatus":{"type":"string"},"entityUrn":{"type":"string"},"tempStatusEmoji":{"type":"string"},"iweWarned":{"type":"boolean"},"publicIdentifier":{"type":"string"},"headline":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.identity.profile.Profile"},"com.linkedin.deco.recipe.anonymous.Anon846022288":{"fields":{"profilePicture":{"type":"com.linkedin.voyager.dash.deco.identity.profile.ProfilePhotoDecoSpecReadOnlyProfilePicture"},"lastName":{"type":"string"},"insight":{"type":"com.linkedin.deco.recipe.anonymous.Anon1479950671","isInjection":true},"firstName":{"type":"string"},"profileProfileActions":{"type":"com.linkedin.voyager.dash.deco.identity.profile.ProfileActionsInjection","isInjection":true},"entityUrn":{"type":"string"},"memberRelationship":{"type":"com.linkedin.voyager.dash.deco.relationships.MemberRelationshipV2ForInjection","isInjection":true},"profileTopPosition":{"type":"com.linkedin.deco.recipe.anonymous.Anon1428941918","isInjection":true},"publicIdentifier":{"type":"string"},"headline":{"type":"string"},"backgroundPicture":{"type":"com.linkedin.voyager.dash.deco.identity.profile.ProfilePhotoDecoSpecReadOnlyBackground"}},"baseType":"com.linkedin.voyager.dash.identity.profile.Profile"},"com.linkedin.voyager.dash.deco.common.image.ImageViewModel":{"fields":{"attributes":{"type":{"array":"com.linkedin.voyager.dash.deco.common.image.ImageAttribute"}},"actionTarget":{"type":"string"},"totalCount":{"type":"int"},"accessibilityTextAttributes":{"type":{"array":"com.linkedin.voyager.dash.deco.common.text.TextAttributeV2"}},"accessibilityText":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.common.image.ImageViewModel"},"com.linkedin.deco.recipe.anonymous.Anon648914460":{"fields":{"companyUrn":{"type":"string"},"company":{"type":"com.linkedin.deco.recipe.anonymous.Anon1927941263","resolvedFrom":"companyUrn"},"vectorImage":{"type":"com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrlAndAttribution"}},"baseType":"com.linkedin.voyager.dash.common.image.NonEntityCompanyLogo"},"com.linkedin.deco.recipe.anonymous.Anon1042323916":{"fields":{"entityUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.jobs.JobPosting"},"com.linkedin.deco.recipe.anonymous.Anon1969742478":{"fields":{"paging":{"type":"com.linkedin.voyager.dash.deco.common.FullPaging"},"metadata":{"type":"com.linkedin.deco.recipe.anonymous.Anon1585981083"},"elements":{"type":{"array":"com.linkedin.deco.recipe.anonymous.Anon1283481334"}}},"baseType":"com.linkedin.restli.common.CollectionResponse"},"com.linkedin.voyager.dash.deco.common.text.Hashtag":{"fields":{"entityUrn":{"type":"string"},"trackingUrn":{"type":"string"},"actionTarget":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.feed.Hashtag"},"com.linkedin.deco.recipe.anonymous.Anon1465360068":{"fields":{"viewingBehavior":{"type":"string"},"url":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.common.text.TextLink"},"com.linkedin.deco.recipe.anonymous.Anon1647280845":{"fields":{"accentType":{"type":"string"},"image":{"type":"com.linkedin.voyager.dash.deco.common.image.ImageViewModel"}},"baseType":"com.linkedin.voyager.dash.launchpad.LaunchpadBranding"},"com.linkedin.voyager.dash.deco.common.FullPaging":{"fields":{"start":{"type":"int"},"count":{"type":"int"},"total":{"type":"int"},"links":{"type":{"array":"com.linkedin.voyager.dash.deco.common.Link"}}},"baseType":"com.linkedin.restli.common.CollectionMetadata"},"com.linkedin.voyager.dash.deco.launchpad.JobSearchQuery":{"fields":{"geo":{"type":"com.linkedin.deco.recipe.anonymous.Anon1271139837","resolvedFrom":"geoUrn"},"keywords":{"type":"string"},"geoUrn":{"type":"string"},"savedSearchId":{"type":"long"}},"baseType":"com.linkedin.voyager.dash.launchpad.attribute.JobSearchQuery"},"com.linkedin.voyager.dash.deco.common.image.ProfessionalEvent":{"fields":{"logoImage":{"type":{"union":{"url":"string","vectorImage":"com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrlAndAttribution"}}},"entityUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.events.ProfessionalEvent"},"com.linkedin.voyager.dash.deco.common.video.Thumbnail":{"fields":{"resolution":{"type":"com.linkedin.voyager.dash.deco.common.video.Resolution"},"url":{"type":"string"}},"baseType":"com.linkedin.videocontent.Thumbnail"},"com.linkedin.voyager.dash.deco.common.DateRange":{"fields":{"start":{"type":"com.linkedin.voyager.dash.deco.common.Date"},"end":{"type":"com.linkedin.voyager.dash.deco.common.Date"}},"baseType":"com.linkedin.common.DateRange"},"com.linkedin.voyager.dash.deco.organization.EmbeddedVideoDecoSpec":{"fields":{"url":{"type":"string"},"thumbnail":{"type":"com.linkedin.voyager.dash.deco.common.VectorImage"}},"baseType":"com.linkedin.voyager.dash.organization.EmbeddedVideo"},"com.linkedin.deco.recipe.anonymous.Anon1670704461":{"fields":{"title":{"type":"string"},"subTitle":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.launchpad.LaunchpadDismissDialog"},"com.linkedin.voyager.dash.deco.common.Date":{"fields":{"month":{"type":"int"},"year":{"type":"int"},"day":{"type":"int"}},"baseType":"com.linkedin.common.Date"},"com.linkedin.voyager.dash.deco.common.video.ProgressiveDownloadMetadata":{"fields":{"streamingLocations":{"type":{"array":"com.linkedin.voyager.dash.deco.common.video.StreamingLocation"}},"size":{"type":"long"},"bitRate":{"type":"int"},"width":{"type":"int"},"mediaType":{"type":"string"},"mimeType":{"type":"string"},"height":{"type":"int"}},"baseType":"com.linkedin.videocontent.ProgressiveDownloadMetadata"},"com.linkedin.deco.recipe.anonymous.Anon1196575529":{"fields":{"entityUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.organization.OrganizationalPage"},"com.linkedin.voyager.dash.deco.organization.OrganizationRoleType":{"fields":{"localizedName":{"type":"string"},"role":{"type":"string"},"paidMediaRole":{"type":"boolean"},"localizedDescription":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.organization.OrganizationRoleType"},"com.linkedin.voyager.dash.deco.common.text.TextViewModelV2":{"fields":{"textDirection":{"type":"string"},"text":{"type":"string"},"attributesV2":{"type":{"array":"com.linkedin.voyager.dash.deco.common.text.TextAttributeV2"}},"accessibilityTextAttributesV2":{"type":{"array":"com.linkedin.voyager.dash.deco.common.text.TextAttributeV2"}},"accessibilityText":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.common.text.TextViewModel"},"com.linkedin.deco.recipe.anonymous.Anon1789236903":{"fields":{"title":{"type":"string"},"entityUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.publishing.ContentSeries"},"com.linkedin.voyager.dash.deco.relationships.MemberRelationshipV2":{"fields":{"memberRelationshipData":{"type":{"union":{"noInvitation":"com.linkedin.deco.recipe.anonymous.Anon1031101697","invitation":"com.linkedin.voyager.dash.deco.relationships.Invitation","connection":"com.linkedin.voyager.dash.deco.relationships.Connection"}}},"entityUrn":{"type":"string"},"memberRelationshipUnion":{"type":{"union":{"self":"com.linkedin.restli.common.EmptyRecord","connection":"com.linkedin.voyager.dash.deco.relationships.Connection","noConnection":"com.linkedin.voyager.dash.deco.relationships.NoConnection"}}}},"baseType":"com.linkedin.voyager.dash.relationships.MemberRelationship"},"com.linkedin.voyager.dash.deco.sponsoredcontent.LeadGenForm":{"fields":{"formSections":{"type":{"array":"com.linkedin.deco.recipe.anonymous.Anon813412436"}},"submitted":{"type":"boolean"},"entityUrn":{"type":"string"},"privacyPolicy":{"type":"com.linkedin.voyager.dash.deco.common.text.TextViewModelV2"},"postSubmissionContent":{"type":"com.linkedin.deco.recipe.anonymous.Anon40184024"},"lastSubmittedAt":{"type":"long"},"trackingMetadata":{"type":"string"},"header":{"type":"com.linkedin.voyager.dash.deco.common.text.TextViewModelV2"},"banner":{"type":"com.linkedin.deco.recipe.anonymous.Anon712430272"},"submitButtonText":{"type":"string"},"customPrivacyPolicy":{"type":"com.linkedin.voyager.dash.deco.common.text.TextViewModelV2"},"consentSection":{"type":"com.linkedin.deco.recipe.anonymous.Anon813412436"}},"baseType":"com.linkedin.voyager.dash.sponsoredcontent.leadgen.LeadGenForm"},"com.linkedin.voyager.dash.deco.relationships.ProfileWithEmailRequired":{"fields":{"memorialized":{"type":"boolean"},"lastName":{"type":"string"},"firstName":{"type":"string"},"tempStatus":{"type":"string"},"entityUrn":{"type":"string"},"tempStatusEmoji":{"type":"string"},"publicIdentifier":{"type":"string"},"headline":{"type":"string"},"emailRequired":{"type":"boolean"}},"baseType":"com.linkedin.voyager.dash.identity.profile.Profile"},"com.linkedin.deco.recipe.anonymous.Anon1975396536":{"fields":{"saved":{"type":"boolean"},"salesListNavigationUrl":{"type":"string"},"entityUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.identity.profile.actions.SalesNavigatorSaveState"},"com.linkedin.deco.recipe.anonymous.Anon929195650":{"fields":{"entityUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.organization.School"},"com.linkedin.deco.recipe.anonymous.Anon1299693827":{"fields":{"paging":{"type":"com.linkedin.voyager.dash.deco.common.FullPaging"},"elements":{"type":{"array":"com.linkedin.deco.recipe.anonymous.Anon1128782547"}}},"baseType":"com.linkedin.restli.common.CollectionResponse"},"com.linkedin.deco.recipe.anonymous.Anon352881287":{"fields":{"entityUrn":{"type":"string"},"emailRequired":{"type":"boolean"}},"baseType":"com.linkedin.voyager.dash.identity.profile.Profile"},"com.linkedin.deco.recipe.anonymous.Anon1760283115":{"fields":{"entityUrn":{"type":"string"},"preDashFollowingInfoUrn":{"type":"string"},"following":{"type":"boolean"}},"baseType":"com.linkedin.voyager.dash.feed.FollowingState"},"com.linkedin.voyager.dash.deco.common.text.LearningCourse":{"fields":{"title":{"type":"string"},"entityUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.learning.LearningCourse"},"com.linkedin.deco.recipe.anonymous.Anon50101142":{"fields":{"ringStatus":{"type":"com.linkedin.deco.recipe.anonymous.Anon1320789737"},"profileUrn":{"type":"string"},"vectorImage":{"type":"com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrlAndAttribution"},"profile":{"type":"com.linkedin.deco.recipe.anonymous.Anon587401631","resolvedFrom":"profileUrn"}},"baseType":"com.linkedin.voyager.dash.common.image.NonEntityProfilePicture"},"com.linkedin.deco.recipe.anonymous.Anon1566936928":{"fields":{"company":{"type":"com.linkedin.deco.recipe.anonymous.Anon1226238669","resolvedFrom":"companyUrn"},"multiLocaleCompanyName":{"type":{"map":"string"}},"entityUrn":{"type":"string"},"dateRange":{"type":"com.linkedin.voyager.dash.deco.common.DateRange"},"companyUrn":{"type":"string"},"companyName":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.identity.profile.Position"},"com.linkedin.deco.recipe.anonymous.Anon1122581856":{"fields":{"paging":{"type":"com.linkedin.voyager.dash.deco.common.FullPaging"},"metadata":{"type":"com.linkedin.deco.recipe.anonymous.Anon1585981083"},"elements":{"type":{"array":"com.linkedin.voyager.dash.deco.organization.Profile"}}},"baseType":"com.linkedin.restli.common.CollectionResponse"},"com.linkedin.voyager.dash.deco.common.image.ImageAttribute":{"fields":{"detailData":{"type":{"union":{"profilePictureWithoutFrame":"com.linkedin.voyager.dash.deco.common.image.ProfileWithoutFrame","profilePicture":"com.linkedin.voyager.dash.deco.common.image.Profile","profilePictureWithRingStatus":"com.linkedin.voyager.dash.deco.common.image.ProfileWithRingStatus","companyLogo":"com.linkedin.voyager.dash.deco.common.image.Company","professionalEventLogo":"com.linkedin.voyager.dash.deco.common.image.ProfessionalEvent","organizationalPageLogo":"com.linkedin.voyager.dash.deco.common.image.OrganizationalPage","schoolLogo":"com.linkedin.voyager.dash.deco.common.image.School","groupLogo":"com.linkedin.voyager.dash.deco.common.image.Group"}},"resolvedFrom":"detailDataUnion"},"tintColor":{"type":"string"},"detailDataUnion":{"type":{"union":{"profilePictureWithoutFrame":"string","profilePictureWithRingStatus":"string","companyLogo":"string","icon":"string","systemImage":"string","nonEntityGroupLogo":"com.linkedin.deco.recipe.anonymous.Anon1436383648","organizationalPageLogo":"string","vectorImage":"com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrlAndAttribution","nonEntityProfessionalEventLogo":"com.linkedin.deco.recipe.anonymous.Anon377984030","profilePicture":"string","imageUrl":"com.linkedin.deco.recipe.anonymous.Anon1529112441","professionalEventLogo":"string","nonEntitySchoolLogo":"com.linkedin.deco.recipe.anonymous.Anon1568806612","nonEntityCompanyLogo":"com.linkedin.deco.recipe.anonymous.Anon648914460","schoolLogo":"string","groupLogo":"string","ghostImage":"string","nonEntityProfilePicture":"com.linkedin.deco.recipe.anonymous.Anon50101142"}}},"tapTargets":{"type":{"array":"com.linkedin.voyager.dash.deco.common.TapTargetWithoutEntity"}},"scalingType":{"type":"string"},"displayAspectRatio":{"type":"double"}},"baseType":"com.linkedin.voyager.dash.common.image.ImageAttribute"},"com.linkedin.deco.recipe.anonymous.Anon1994177525":{"fields":{"paging":{"type":"com.linkedin.voyager.dash.deco.common.FullPaging"},"elements":{"type":{"array":"com.linkedin.deco.recipe.anonymous.Anon743011996"}}},"baseType":"com.linkedin.restli.common.CollectionResponse"},"com.linkedin.voyager.dash.deco.common.image.ProfileWithRingStatus":{"fields":{"ringStatus":{"type":"com.linkedin.deco.recipe.anonymous.Anon1080314395","isInjection":true},"profilePicture":{"type":"com.linkedin.voyager.dash.deco.common.image.PhotoFilterPicture"},"entityUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.identity.profile.Profile"},"com.linkedin.voyager.dash.deco.common.image.PhotoFilterPicture":{"fields":{"displayImageWithFrameReferenceUnion":{"type":{"union":{"url":"string","vectorImage":"com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrlAndAttribution"}}},"a11yText":{"type":"string"},"displayImageReference":{"type":{"union":{"url":"string","vectorImage":"com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrlAndAttribution"}}}},"baseType":"com.linkedin.voyager.dash.identity.profile.PhotoFilterPicture"},"com.linkedin.deco.recipe.anonymous.Anon1447917113":{"fields":{"insightImage":{"type":"com.linkedin.voyager.dash.deco.common.image.ImageViewModel"},"text":{"type":"com.linkedin.voyager.dash.deco.common.text.TextViewModelV2"},"navigationUrl":{"type":"string"},"entityUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.relationships.Insight"},"com.linkedin.voyager.dash.deco.common.text.Company":{"fields":{"name":{"type":"string"},"entityUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.organization.Company"},"com.linkedin.deco.recipe.anonymous.Anon735489647":{"fields":{"entityUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.identity.notifications.edgesetting.EdgeSetting"},"com.linkedin.deco.recipe.anonymous.Anon1927941263":{"fields":{"entityUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.organization.Company"},"com.linkedin.voyager.dash.deco.common.image.ProfileWithoutFrame":{"fields":{"profilePicture":{"type":"com.linkedin.voyager.dash.deco.common.image.PhotoFilterPicture"},"entityUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.identity.profile.Profile"},"com.linkedin.deco.recipe.anonymous.Anon587401631":{"fields":{"entityUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.identity.profile.Profile"},"com.linkedin.deco.recipe.anonymous.Anon792975169":{"fields":{"dashLeadGenFormUrn":{"type":"string"},"privacyPolicyUrl":{"type":"string"},"dashLeadGenForm":{"type":"com.linkedin.voyager.dash.deco.sponsoredcontent.LeadGenForm","resolvedFrom":"dashLeadGenFormUrn"},"organizationProductCallToAction":{"type":"com.linkedin.deco.recipe.anonymous.Anon625674184"},"leadGenFormUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.organization.OrganizationProductLeadGenFormCallToAction"},"com.linkedin.deco.recipe.anonymous.Anon1621960601":{"fields":{"name":{"type":"string"},"logo":{"type":{"union":{"url":"string","vectorImage":"com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrlAndAttribution"}}},"entityUrn":{"type":"string"},"url":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.organization.School"},"com.linkedin.deco.recipe.anonymous.Anon199392175":{"fields":{"paidInMail":{"type":"boolean"},"recipient":{"type":{"map":"com.linkedin.deco.recipe.anonymous.Anon587401631"},"resolvedFrom":"recipientUrns"},"messageRequestContextUrn":{"type":"string"},"recipientUrns":{"type":{"array":"string"}},"targetUrl":{"type":"string"},"existingConversation":{"type":"com.linkedin.deco.recipe.anonymous.Anon807183080","resolvedFrom":"existingConversationUrn"},"existingConversationUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.messaging.compose.ComposeNavigationContext"},"com.linkedin.deco.recipe.anonymous.Anon1320789737":{"fields":{"ringContentType":{"type":"string"},"actionTarget":{"type":"string"},"preDashEntityUrn":{"type":"string"},"entityUrn":{"type":"string"},"emphasized":{"type":"boolean"}},"baseType":"com.linkedin.voyager.dash.common.image.RingStatus"},"com.linkedin.deco.recipe.anonymous.Anon721197842":{"fields":{"paging":{"type":"com.linkedin.voyager.dash.deco.common.FullPaging"},"elements":{"type":{"array":"com.linkedin.deco.recipe.anonymous.Anon1128782547"}}},"baseType":"com.linkedin.restli.common.CollectionResponse"},"com.linkedin.deco.recipe.anonymous.Anon1085906135":{"fields":{"multiLocaleCompanyName":{"type":{"map":"string"}},"entityUrn":{"type":"string"},"dateRange":{"type":"com.linkedin.voyager.dash.deco.common.DateRange"},"companyName":{"type":"string"},"company":{"type":"com.linkedin.deco.recipe.anonymous.Anon184130218","resolvedFrom":"companyUrn"},"title":{"type":"string"},"companyUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.identity.profile.Position"},"com.linkedin.deco.recipe.anonymous.Anon842053443":{"fields":{"followerResolutionResult":{"type":"com.linkedin.deco.recipe.anonymous.Anon846022288","resolvedFrom":"follower"},"followedAt":{"type":"com.linkedin.voyager.dash.deco.common.text.TextViewModelV2"},"follower":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.organization.OrganizationFollower"},"com.linkedin.deco.recipe.anonymous.Anon807183080":{"fields":{"entityUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.messaging.Conversation"},"com.linkedin.deco.recipe.anonymous.Anon570745354":{"fields":{"name":{"type":"string"},"logo":{"type":{"union":{"url":"string","vectorImage":"com.linkedin.voyager.dash.deco.common.VectorImage"}}},"entityUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.organization.Company"},"com.linkedin.voyager.dash.deco.common.image.Profile":{"fields":{"profilePicture":{"type":"com.linkedin.voyager.dash.deco.common.image.PhotoFilterPicture"},"entityUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.identity.profile.Profile"},"com.linkedin.voyager.dash.deco.common.text.JobPosting":{"fields":{"title":{"type":"string"},"entityUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.jobs.JobPosting"},"com.linkedin.voyager.dash.deco.common.text.TextAttributeV2":{"fields":{"start":{"type":"int"},"length":{"type":"int"},"detailData":{"type":{"union":{"jobPostingName":"com.linkedin.voyager.dash.deco.common.text.JobPosting","profileFamiliarName":"com.linkedin.voyager.dash.deco.common.text.ProfileForFamiliarName","groupName":"com.linkedin.deco.recipe.anonymous.Anon163061530","profileFullName":"com.linkedin.voyager.dash.deco.common.text.ProfileForFullName","learningCourseName":"com.linkedin.voyager.dash.deco.common.text.LearningCourse","companyName":"com.linkedin.voyager.dash.deco.common.text.Company","profileMention":"com.linkedin.voyager.dash.deco.common.text.ProfileForMention","schoolName":"com.linkedin.voyager.dash.deco.common.text.School","organizationalPageName":"com.linkedin.voyager.dash.deco.common.text.OrganizationalPage","hashtag":"com.linkedin.voyager.dash.deco.common.text.Hashtag"}},"resolvedFrom":"detailDataUnion"},"detailDataUnion":{"type":{"union":{"jobPostingName":"string","profileFamiliarName":"string","hyperlink":"string","color":"string","companyName":"string","icon":"string","systemImage":"string","epoch":"com.linkedin.deco.recipe.anonymous.Anon858976209","organizationalPageName":"string","textLink":"com.linkedin.deco.recipe.anonymous.Anon1465360068","listItemStyle":"com.linkedin.deco.recipe.anonymous.Anon409680083","hyperlinkOpenExternally":"string","listStyle":"string","groupName":"string","profileFullName":"string","stringFieldReference":"com.linkedin.deco.recipe.anonymous.Anon1251747613","learningCourseName":"string","profileMention":"string","style":"string","schoolName":"string","hashtag":"string"}}}},"baseType":"com.linkedin.voyager.dash.common.text.TextAttribute"},"com.linkedin.deco.recipe.anonymous.Anon1213132949":{"fields":{"entityUrn":{"type":"string"},"memberRelationshipUnion":{"type":{"union":{"self":"com.linkedin.restli.common.EmptyRecord","connection":"com.linkedin.deco.recipe.anonymous.Anon2134644859","noConnection":"com.linkedin.deco.recipe.anonymous.Anon1843097075"}}}},"baseType":"com.linkedin.voyager.dash.relationships.MemberRelationship"},"com.linkedin.voyager.dash.deco.common.ux.RelationshipActionData":{"fields":{"relationshipsTrackingId":{"type":"bytes"},"relationshipData":{"type":{"union":{"connectionOrInvitation":"com.linkedin.voyager.dash.deco.relationships.MemberRelationshipV2","memberToEntityRelationship":"com.linkedin.voyager.dash.deco.relationships.DirectionalEntityRelationship"}},"resolvedFrom":"relationshipDataUnion"},"relationshipDataUnion":{"type":{"union":{"connectionOrInvitation":"string","memberToEntityRelationship":"string"}}},"moduleKey":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.common.relationships.RelationshipActionData"},"com.linkedin.voyager.dash.deco.identity.profile.MemberRelationshipWrapper":{"fields":{"memberRelationshipUrn":{"type":"string"},"memberRelationship":{"type":"com.linkedin.voyager.dash.deco.relationships.MemberRelationshipV2","resolvedFrom":"memberRelationshipUrn"}},"baseType":"com.linkedin.voyager.dash.relationships.MemberRelationshipWrapper"},"com.linkedin.deco.recipe.anonymous.Anon191738356":{"fields":{"metadataUnion":{"type":{"union":{"memberToMemberFollow":"com.linkedin.deco.recipe.anonymous.Anon198476569","memberToCompanyFollow":"com.linkedin.deco.recipe.anonymous.Anon378816379"}}},"followingStateUrn":{"type":"string"},"followingState":{"type":"com.linkedin.voyager.dash.deco.feed.FollowingState","resolvedFrom":"followingStateUrn"}},"baseType":"com.linkedin.voyager.dash.relationships.FollowRelationship"},"com.linkedin.deco.recipe.anonymous.Anon2116040434":{"fields":{"company":{"type":"com.linkedin.voyager.dash.deco.organization.MiniCompany","resolvedFrom":"companyUrn"},"title":{"type":"string"},"multiLocaleTitle":{"type":{"map":"string"}},"entityUrn":{"type":"string"},"companyUrn":{"type":"string"},"companyName":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.identity.profile.Position"},"com.linkedin.deco.recipe.anonymous.Anon856218111":{"fields":{"transcribedDocumentUrl":{"type":"string"},"urn":{"type":"string"},"manifestUrl":{"type":"string"},"scanRequiredForDownload":{"type":"boolean"},"totalPageCount":{"type":"int"},"manifestUrlExpiresAt":{"type":"long"},"title":{"type":"string"},"coverPages":{"type":"com.linkedin.deco.recipe.anonymous.Anon1636615691"},"transcribedDocumentUrlExpiresAt":{"type":"long"}},"baseType":"com.linkedin.documentcontent.Document"},"com.linkedin.deco.recipe.anonymous.Anon1436383648":{"fields":{"groupUrn":{"type":"string"},"vectorImage":{"type":"com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrlAndAttribution"},"group":{"type":"com.linkedin.deco.recipe.anonymous.Anon1869367056","resolvedFrom":"groupUrn"}},"baseType":"com.linkedin.voyager.dash.common.image.NonEntityGroupLogo"},"com.linkedin.deco.recipe.anonymous.Anon1361453782":{"fields":{"paging":{"type":"com.linkedin.voyager.dash.deco.common.FullPaging"},"elements":{"type":{"array":"com.linkedin.deco.recipe.anonymous.Anon743011996"}}},"baseType":"com.linkedin.restli.common.CollectionResponse"},"com.linkedin.deco.recipe.anonymous.Anon1861880920":{"fields":{"paging":{"type":"com.linkedin.voyager.dash.deco.common.FullPaging"},"elements":{"type":{"array":"com.linkedin.deco.recipe.anonymous.Anon1085906135"}}},"baseType":"com.linkedin.restli.common.CollectionResponse"},"com.linkedin.deco.recipe.anonymous.Anon1585981083":{"fields":{"title":{"type":"string"},"description":{"type":"string"},"connectionsUsingProductTypeUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.identity.profile.ConnectionsUsingProductMetadata"},"com.linkedin.deco.recipe.anonymous.Anon2134644859":{"fields":{"entityUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.relationships.Connection"}}}},"included":[]}
</code>
<code style="display: none" id="datalet-bpr-guid-104263">
  {"request":"/voyager/api/voyagerLaunchpadDashLaunchpadViews?decorationId\u003Dcom.linkedin.voyager.dash.deco.launchpad.LaunchpadView-65\u0026launchpadContext\u003DTAKEOVER\u0026q\u003Dcontext","status":200,"body":"bpr-guid-104263","method":"GET","headers":{"x-li-uuid":"AAX9pWM/tcB+TnflXcw30Q\u003D\u003D"}}
</code>
<img src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" style="display: none" class="datalet-bpr-guid-104263"><code style="display: none" id="bpr-guid-104265">
  {"data":{"statuses":{},"results":{"*urn:li:fsd_featureAccess:CAN_ACCESS_ADVERTISE_BADGE":"urn:li:fsd_featureAccess:CAN_ACCESS_ADVERTISE_BADGE","*urn:li:fsd_featureAccess:CAN_ACCESS_SALES_NAV_BADGE":"urn:li:fsd_featureAccess:CAN_ACCESS_SALES_NAV_BADGE"},"errors":{}},"included":[{"featureAccessType":"CAN_ACCESS_SALES_NAV_BADGE","entityUrn":"urn:li:fsd_featureAccess:CAN_ACCESS_SALES_NAV_BADGE","hasAccess":false,"$type":"com.linkedin.voyager.dash.premium.FeatureAccess"},{"featureAccessType":"CAN_ACCESS_ADVERTISE_BADGE","entityUrn":"urn:li:fsd_featureAccess:CAN_ACCESS_ADVERTISE_BADGE","hasAccess":false,"$type":"com.linkedin.voyager.dash.premium.FeatureAccess"}]}
</code>
<code style="display: none" id="datalet-bpr-guid-104265">
  {"request":"/voyager/api/voyagerPremiumDashFeatureAccess?ids\u003DList(urn%3Ali%3Afsd_featureAccess%3ACAN_ACCESS_SALES_NAV_BADGE,urn%3Ali%3Afsd_featureAccess%3ACAN_ACCESS_ADVERTISE_BADGE)","status":200,"body":"bpr-guid-104265","method":"GET","headers":{"x-li-uuid":"AAX9pWM/tcB+TnflXcw30Q\u003D\u003D"}}
</code>
<img src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" style="display: none" class="datalet-bpr-guid-104265"><code style="display: none" id="bpr-guid-104267">
  {"data":{"entityUrn":"urn:li:collectionResponse:7ZvAwvPwYldk7Tvl3jXgC4ymrtxthgc+3EdE7ncMd98=","elements":[{"count":0,"tab":"NOTIFICATIONS","$type":"com.linkedin.voyager.common.communications.TabBadge"},{"count":0,"tab":"MESSAGING","$type":"com.linkedin.voyager.common.communications.TabBadge"},{"count":0,"tab":"MY_NETWORK","$type":"com.linkedin.voyager.common.communications.TabBadge"}],"paging":{"count":10,"start":0,"links":[]},"$type":"com.linkedin.restli.common.CollectionResponse"},"included":[]}
</code>
<code style="display: none" id="datalet-bpr-guid-104267">
  {"request":"/voyager/api/voyagerCommunicationsTabBadges?q\u003DtabBadges\u0026countFrom\u003D0","status":200,"body":"bpr-guid-104267","method":"GET","headers":{"x-li-uuid":"AAX9pWM/tcB+TnflXcw30Q\u003D\u003D"}}
</code>
<img src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" style="display: none" class="datalet-bpr-guid-104267"><code style="display: none" id="bpr-guid-104270">
  {"data":{"canBrowseProfiles":false,"reactivationFeaturesEligible":false,"canViewJobAnalytics":false,"canViewWVMP":false,"premiumFreeTrialEligible":true,"canAccessLearningVideos":false,"premiumLearningUpgradeEligible":false,"canViewCompanyInsights":false,"$type":"com.linkedin.voyager.premium.FeatureAccess"},"included":[]}
</code>
<code style="display: none" id="datalet-bpr-guid-104270">
  {"request":"/voyager/api/premium/featureAccess?name\u003DreactivationFeaturesEligible","status":200,"body":"bpr-guid-104270","method":"GET","headers":{"x-li-uuid":"AAX9pWM/tcB+TnflXcw30Q\u003D\u003D"}}
</code>
<img src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" style="display: none" class="datalet-bpr-guid-104270"><code style="display: none" id="bpr-guid-104273">
  {"data":{"entityUrn":"urn:li:collectionResponse:dbIx7MsYORcVsKofdD+ilcmRKXjnSjrc4kO6tV3EIyg=","paging":{"count":10,"start":0,"links":[]},"*elements":["urn:li:fsd_profile:ACoAAC9P7scB1yv1hA-ZjtKBAxcuNQvmvu08uhI"],"$type":"com.linkedin.restli.common.CollectionResponse"},"meta":{"microSchema":{"version":"2","types":{"com.linkedin.voyager.dash.deco.common.text.TextViewModelV2":{"fields":{"textDirection":{"type":"string"},"text":{"type":"string"},"attributesV2":{"type":{"array":"com.linkedin.voyager.dash.deco.common.text.TextAttributeV2"}},"accessibilityTextAttributesV2":{"type":{"array":"com.linkedin.voyager.dash.deco.common.text.TextAttributeV2"}},"accessibilityText":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.common.text.TextViewModel"},"com.linkedin.deco.recipe.anonymous.Anon1080314395":{"fields":{"ringContentType":{"type":"string"},"actionTarget":{"type":"string"},"preDashEntityUrn":{"type":"string"},"entityUrn":{"type":"string"},"emphasized":{"type":"boolean"}},"baseType":"com.linkedin.voyager.dash.common.image.RingStatus"},"com.linkedin.deco.recipe.anonymous.Anon1529112441":{"fields":{"originalImageUrl":{"type":"string"},"originalHeight":{"type":"int"},"url":{"type":"string"},"originalWidth":{"type":"int"}},"baseType":"com.linkedin.voyager.dash.common.ImageUrl"},"com.linkedin.voyager.dash.deco.relationships.ProfileWithEmailRequired":{"fields":{"memorialized":{"type":"boolean"},"lastName":{"type":"string"},"firstName":{"type":"string"},"tempStatus":{"type":"string"},"entityUrn":{"type":"string"},"tempStatusEmoji":{"type":"string"},"publicIdentifier":{"type":"string"},"headline":{"type":"string"},"emailRequired":{"type":"boolean"}},"baseType":"com.linkedin.voyager.dash.identity.profile.Profile"},"com.linkedin.deco.recipe.anonymous.Anon377984030":{"fields":{"professionalEvent":{"type":"com.linkedin.deco.recipe.anonymous.Anon1213723597","resolvedFrom":"professionalEventUrn"},"vectorImage":{"type":"com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrlAndAttribution"},"professionalEventUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.common.image.NonEntityProfessionalEventLogo"},"com.linkedin.deco.recipe.anonymous.Anon929195650":{"fields":{"entityUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.organization.School"},"com.linkedin.voyager.dash.deco.common.image.Company":{"fields":{"logo":{"type":{"union":{"url":"string","vectorImage":"com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrlAndAttribution"}}},"entityUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.organization.Company"},"com.linkedin.voyager.dash.deco.common.ux.LabelViewModel":{"fields":{"colorStyle":{"type":"string"},"text":{"type":"com.linkedin.voyager.dash.deco.common.text.TextViewModelV2"}},"baseType":"com.linkedin.voyager.dash.common.ux.label.LabelViewModel"},"com.linkedin.deco.recipe.anonymous.Anon405167834":{"fields":{"name":{"type":"com.linkedin.voyager.dash.deco.common.text.TextViewModelV2"},"nameSupplementaryInfo":{"type":"com.linkedin.voyager.dash.deco.common.text.TextViewModelV2"},"imageUnion":{"type":{"union":{"url":"string","vectorImage":"com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrlAndAttribution"}}},"headline":{"type":"com.linkedin.voyager.dash.deco.common.text.TextViewModelV2"},"subHeadline":{"type":"com.linkedin.voyager.dash.deco.common.text.TextViewModelV2"}},"baseType":"com.linkedin.voyager.dash.common.media.StickerLinkMediumTemplateView"},"com.linkedin.deco.recipe.anonymous.Anon409680083":{"fields":{"type":{"type":"string"},"index":{"type":"int"}},"baseType":"com.linkedin.voyager.dash.common.text.ListItemStyle"},"com.linkedin.voyager.dash.deco.relationships.Invitation":{"fields":{"inviteeMemberResolutionResult":{"type":"com.linkedin.deco.recipe.anonymous.Anon336652209","resolvedFrom":"inviteeMember"},"invitationType":{"type":"string"},"inviteeMember":{"type":"string"},"entityUrn":{"type":"string"},"invitationState":{"type":"string"},"invitationId":{"type":"long"},"sharedSecret":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.relationships.invitation.Invitation"},"com.linkedin.deco.recipe.anonymous.Anon918376989":{"fields":{"title":{"type":"string"},"invitationRelationshipOptions":{"type":{"array":"com.linkedin.deco.recipe.anonymous.Anon934606613"}},"subtitle":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.relationships.invitation.InvitationRelationshipForm"},"com.linkedin.voyager.dash.deco.common.Locale":{"fields":{"variant":{"type":"string"},"country":{"type":"string"},"language":{"type":"string"}},"baseType":"com.linkedin.common.Locale"},"com.linkedin.deco.recipe.anonymous.Anon732397008":{"fields":{"headlineVersion":{"type":"com.linkedin.voyager.dash.deco.common.ux.LabelViewModel"},"dismissCta":{"type":"com.linkedin.voyager.dash.deco.common.ux.ButtonAppearance"},"primaryCtaAccessibilityText":{"type":"string"},"dismissCtaButton":{"type":"com.linkedin.deco.recipe.anonymous.Anon1528523240"},"description":{"type":"com.linkedin.voyager.dash.deco.common.text.TextViewModelV2"},"legoTrackingToken":{"type":"string"},"primaryCta":{"type":"com.linkedin.voyager.dash.deco.common.ux.ButtonAppearance"},"primaryCtaButtonV2":{"type":"com.linkedin.voyager.dash.deco.identity.profile.tetris.NavigationAction"},"headline":{"type":"com.linkedin.voyager.dash.deco.common.text.TextViewModelV2"},"dismissCtaAccessibilityText":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.identity.profile.ProfileGeneratedSuggestionPromoCard"},"com.linkedin.deco.recipe.anonymous.Anon1247784858":{"fields":{"badgeIcon":{"type":"string"},"badgeText":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.identity.profile.TopVoiceBadge"},"com.linkedin.deco.recipe.anonymous.Anon934606613":{"fields":{"type":{"type":"string"},"name":{"type":"string"},"controlName":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.relationships.invitation.InvitationRelationshipOption"},"com.linkedin.voyager.dash.deco.common.TapTargetWithoutEntity":{"fields":{"stickerLinkViewUnion":{"type":{"union":{"mediumTemplate":"com.linkedin.deco.recipe.anonymous.Anon405167834","largeTemplate":"com.linkedin.deco.recipe.anonymous.Anon173266477","smallTemplate":"com.linkedin.deco.recipe.anonymous.Anon655007389"}}},"stickerLinkTemplateSize":{"type":"string"},"firstCornerXOffsetPercentage":{"type":"float"},"type":{"type":"string"},"thirdCornerYOffsetPercentage":{"type":"float"},"url":{"type":"string"},"urn":{"type":"string"},"thirdCornerXOffsetPercentage":{"type":"float"},"secondCornerYOffsetPercentage":{"type":"float"},"fourthCornerXOffsetPercentage":{"type":"float"},"firstCornerYOffsetPercentage":{"type":"float"},"untaggable":{"type":"boolean"},"rank":{"type":"int"},"text":{"type":"string"},"fourthCornerYOffsetPercentage":{"type":"float"},"secondCornerXOffsetPercentage":{"type":"float"}},"baseType":"com.linkedin.voyager.dash.common.TapTarget"},"com.linkedin.voyager.dash.deco.common.text.LearningCourse":{"fields":{"title":{"type":"string"},"entityUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.learning.LearningCourse"},"com.linkedin.deco.recipe.anonymous.Anon50101142":{"fields":{"ringStatus":{"type":"com.linkedin.deco.recipe.anonymous.Anon1320789737"},"profileUrn":{"type":"string"},"vectorImage":{"type":"com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrlAndAttribution"},"profile":{"type":"com.linkedin.deco.recipe.anonymous.Anon587401631","resolvedFrom":"profileUrn"}},"baseType":"com.linkedin.voyager.dash.common.image.NonEntityProfilePicture"},"com.linkedin.voyager.dash.deco.common.text.ProfileForFamiliarName":{"fields":{"lastName":{"type":"string"},"firstName":{"type":"string"},"entityUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.identity.profile.Profile"},"com.linkedin.deco.recipe.anonymous.Anon173266477":{"fields":{"nameSupplementaryInfo":{"type":"com.linkedin.voyager.dash.deco.common.text.TextViewModelV2"},"footerText":{"type":"com.linkedin.voyager.dash.deco.common.text.TextViewModelV2"},"imageUnion":{"type":{"union":{"url":"string","vectorImage":"com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrlAndAttribution"}}},"subHeadline":{"type":"com.linkedin.voyager.dash.deco.common.text.TextViewModelV2"},"name":{"type":"com.linkedin.voyager.dash.deco.common.text.TextViewModelV2"},"insightText":{"type":"com.linkedin.voyager.dash.deco.common.text.TextViewModelV2"},"headline":{"type":"com.linkedin.voyager.dash.deco.common.text.TextViewModelV2"},"backgroundImageUnion":{"type":{"union":{"url":"string","vectorImage":"com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrlAndAttribution"}}}},"baseType":"com.linkedin.voyager.dash.common.media.StickerLinkLargeTemplateView"},"com.linkedin.voyager.dash.deco.common.image.OrganizationalPage":{"fields":{"entityUrn":{"type":"string"},"pageType":{"type":"string"},"logoV2":{"type":"com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrlAndAttribution"}},"baseType":"com.linkedin.voyager.dash.organization.OrganizationalPage"},"com.linkedin.voyager.dash.deco.identity.profile.ProfilePhotoDecoSpecEditableProfilePicture":{"fields":{"displayImageWithFrameReferenceUnion":{"type":{"union":{"url":"string","vectorImage":"com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrlAndAttribution"}}},"originalImageUrn":{"type":"string"},"originalImageReference":{"type":{"union":{"url":"string","vectorImage":"com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrlAndAttribution"}}},"a11yText":{"type":"string"},"displayImageReference":{"type":{"union":{"url":"string","vectorImage":"com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrlAndAttribution"}}},"frameType":{"type":"string"},"photoFilterEditInfo":{"type":"com.linkedin.deco.recipe.anonymous.Anon1309211116"},"displayImageUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.identity.profile.PhotoFilterPicture"},"com.linkedin.voyager.dash.deco.identity.profile.ProfilePhotoDecoSpecReadOnlyProfilePicture":{"fields":{"displayImageWithFrameReferenceUnion":{"type":{"union":{"url":"string","vectorImage":"com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrlAndAttribution"}}},"frameType":{"type":"string"},"a11yText":{"type":"string"},"displayImageUrn":{"type":"string"},"displayImageReference":{"type":{"union":{"url":"string","vectorImage":"com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrlAndAttribution"}}}},"baseType":"com.linkedin.voyager.dash.identity.profile.PhotoFilterPicture"},"com.linkedin.deco.recipe.anonymous.Anon1967775378":{"fields":{"paging":{"type":"com.linkedin.voyager.dash.deco.common.FullPaging"},"elements":{"type":{"array":"com.linkedin.deco.recipe.anonymous.Anon732397008"}}},"baseType":"com.linkedin.restli.common.CollectionResponse"},"com.linkedin.voyager.dash.deco.common.Link":{"fields":{"type":{"type":"string"},"rel":{"type":"string"},"href":{"type":"string"}},"baseType":"com.linkedin.restli.common.Link"},"com.linkedin.voyager.dash.deco.common.LocaleExtensionsFull":{"fields":{"x":{"type":"string"},"t":{"type":"string"},"u":{"type":"string"}},"baseType":"com.linkedin.common.LocaleExtensions"},"com.linkedin.deco.recipe.anonymous.Anon858976209":{"fields":{"type":{"type":"string"},"epochAt":{"type":"long"}},"baseType":"com.linkedin.voyager.dash.common.text.EpochTime"},"com.linkedin.voyager.dash.deco.common.image.School":{"fields":{"logo":{"type":{"union":{"url":"string","vectorImage":"com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrlAndAttribution"}}},"entityUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.organization.School"},"com.linkedin.voyager.dash.deco.common.image.ImageAttribute":{"fields":{"detailData":{"type":{"union":{"profilePictureWithoutFrame":"com.linkedin.voyager.dash.deco.common.image.ProfileWithoutFrame","profilePicture":"com.linkedin.voyager.dash.deco.common.image.Profile","profilePictureWithRingStatus":"com.linkedin.voyager.dash.deco.common.image.ProfileWithRingStatus","companyLogo":"com.linkedin.voyager.dash.deco.common.image.Company","professionalEventLogo":"com.linkedin.voyager.dash.deco.common.image.ProfessionalEvent","organizationalPageLogo":"com.linkedin.voyager.dash.deco.common.image.OrganizationalPage","schoolLogo":"com.linkedin.voyager.dash.deco.common.image.School","groupLogo":"com.linkedin.voyager.dash.deco.common.image.Group"}},"resolvedFrom":"detailDataUnion"},"tintColor":{"type":"string"},"detailDataUnion":{"type":{"union":{"profilePictureWithoutFrame":"string","profilePictureWithRingStatus":"string","companyLogo":"string","icon":"string","systemImage":"string","nonEntityGroupLogo":"com.linkedin.deco.recipe.anonymous.Anon1436383648","organizationalPageLogo":"string","vectorImage":"com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrlAndAttribution","nonEntityProfessionalEventLogo":"com.linkedin.deco.recipe.anonymous.Anon377984030","profilePicture":"string","imageUrl":"com.linkedin.deco.recipe.anonymous.Anon1529112441","professionalEventLogo":"string","nonEntitySchoolLogo":"com.linkedin.deco.recipe.anonymous.Anon1568806612","nonEntityCompanyLogo":"com.linkedin.deco.recipe.anonymous.Anon648914460","schoolLogo":"string","groupLogo":"string","ghostImage":"string","nonEntityProfilePicture":"com.linkedin.deco.recipe.anonymous.Anon50101142"}}},"tapTargets":{"type":{"array":"com.linkedin.voyager.dash.deco.common.TapTargetWithoutEntity"}},"scalingType":{"type":"string"},"displayAspectRatio":{"type":"double"}},"baseType":"com.linkedin.voyager.dash.common.image.ImageAttribute"},"com.linkedin.voyager.dash.deco.common.ux.ButtonAppearance":{"fields":{"premiumStyle":{"type":"boolean"},"size":{"type":"string"},"icon":{"type":"string"},"text":{"type":"string"},"iconAfterText":{"type":"boolean"},"emphasize":{"type":"boolean"},"category":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.common.ux.button.ButtonAppearance"},"com.linkedin.voyager.dash.deco.identity.profile.tetris.NavigationAction":{"fields":{"buttonPlacement":{"type":"string"},"legoTrackingId":{"type":"string"},"buttonAppearance":{"type":"com.linkedin.voyager.dash.deco.common.ux.ButtonAppearance"},"icon":{"type":"com.linkedin.voyager.dash.deco.common.image.ImageViewModel"},"actionControlName":{"type":"string"},"text":{"type":"com.linkedin.voyager.dash.deco.common.text.TextViewModelV2"},"actionTarget":{"type":"string"},"accessibilityText":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.identity.profile.tetris.NavigationAction"},"com.linkedin.voyager.dash.deco.common.Coordinate2DFull":{"fields":{"x":{"type":"double"},"y":{"type":"double"}},"baseType":"com.linkedin.common.Coordinate2D"},"com.linkedin.voyager.dash.deco.common.image.ProfileWithRingStatus":{"fields":{"ringStatus":{"type":"com.linkedin.deco.recipe.anonymous.Anon1080314395","isInjection":true},"profilePicture":{"type":"com.linkedin.voyager.dash.deco.common.image.PhotoFilterPicture"},"entityUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.identity.profile.Profile"},"com.linkedin.voyager.dash.deco.relationships.Connection":{"fields":{"createdAt":{"type":"long"},"connectedMemberResolutionResult":{"type":"com.linkedin.deco.recipe.anonymous.Anon336652209","resolvedFrom":"connectedMember"},"connectedMember":{"type":"string"},"entityUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.relationships.Connection"},"com.linkedin.deco.recipe.anonymous.Anon1140274151":{"fields":{"creatorWebsite":{"type":"com.linkedin.voyager.dash.deco.common.text.TextViewModelV2"},"associatedHashtagsCopy":{"type":"com.linkedin.voyager.dash.deco.common.text.TextViewModelV2"},"associatedHashtag":{"type":{"map":"com.linkedin.deco.recipe.anonymous.Anon462674420"},"resolvedFrom":"associatedHashtagUrns"},"associatedHashtagUrns":{"type":{"array":"string"}},"creatorPostAnalytics":{"type":"com.linkedin.deco.recipe.anonymous.Anon1253450705"}},"baseType":"com.linkedin.voyager.dash.identity.profile.CreatorInfo"},"com.linkedin.deco.recipe.anonymous.Anon1253450705":{"fields":{"description":{"type":"com.linkedin.voyager.dash.deco.common.text.TextViewModelV2"},"totalCount":{"type":"long"},"title":{"type":"com.linkedin.voyager.dash.deco.common.text.TextViewModelV2"},"percentageChange":{"type":"double"}},"baseType":"com.linkedin.voyager.dash.identity.profile.CreatorPostAnalytics"},"com.linkedin.voyager.dash.deco.common.image.PhotoFilterPicture":{"fields":{"displayImageWithFrameReferenceUnion":{"type":{"union":{"url":"string","vectorImage":"com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrlAndAttribution"}}},"a11yText":{"type":"string"},"displayImageReference":{"type":{"union":{"url":"string","vectorImage":"com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrlAndAttribution"}}}},"baseType":"com.linkedin.voyager.dash.identity.profile.PhotoFilterPicture"},"com.linkedin.deco.recipe.anonymous.Anon1309211116":{"fields":{"saturation":{"type":"double"},"bottomLeft":{"type":"com.linkedin.voyager.dash.deco.common.Coordinate2DFull"},"vignette":{"type":"double"},"brightness":{"type":"double"},"photoFilterType":{"type":"string"},"bottomRight":{"type":"com.linkedin.voyager.dash.deco.common.Coordinate2DFull"},"topLeft":{"type":"com.linkedin.voyager.dash.deco.common.Coordinate2DFull"},"contrast":{"type":"double"},"topRight":{"type":"com.linkedin.voyager.dash.deco.common.Coordinate2DFull"}},"baseType":"com.linkedin.voyager.dash.identity.profile.PhotoFilterEditInfo"},"com.linkedin.voyager.dash.deco.common.image.Group":{"fields":{"logo":{"type":{"union":{"url":"string","vectorImage":"com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrlAndAttribution"}}},"entityUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.groups.Group"},"com.linkedin.deco.recipe.anonymous.Anon1918694303":{"fields":{"entityUrn":{"type":"string"},"defaultLocalizedName":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.common.Geo"},"com.linkedin.voyager.dash.deco.common.text.Company":{"fields":{"name":{"type":"string"},"entityUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.organization.Company"},"com.linkedin.deco.recipe.anonymous.Anon1213723597":{"fields":{"entityUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.events.ProfessionalEvent"},"com.linkedin.voyager.dash.deco.identity.profile.ProfilePhotoDecoSpecEditableBackgroundPicture":{"fields":{"originalImageUrn":{"type":"string"},"originalImageReference":{"type":{"union":{"url":"string","vectorImage":"com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrlAndAttribution"}}},"photoFilterEditInfo":{"type":"com.linkedin.deco.recipe.anonymous.Anon1309211116"},"displayImageUrn":{"type":"string"},"displayImageReference":{"type":{"union":{"url":"string","vectorImage":"com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrlAndAttribution"}}}},"baseType":"com.linkedin.voyager.dash.identity.profile.PhotoFilterPicture"},"com.linkedin.deco.recipe.anonymous.Anon655007389":{"fields":{"name":{"type":"com.linkedin.voyager.dash.deco.common.text.TextViewModelV2"},"imageUnion":{"type":{"union":{"url":"string","vectorImage":"com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrlAndAttribution"}}}},"baseType":"com.linkedin.voyager.dash.common.media.StickerLinkSmallTemplateView"},"com.linkedin.deco.recipe.anonymous.Anon1745422644":{"fields":{"countryUrn":{"type":"string"},"country":{"type":"com.linkedin.deco.recipe.anonymous.Anon1918694303","resolvedFrom":"countryUrn"},"defaultLocalizedNameWithoutCountryName":{"type":"string"},"entityUrn":{"type":"string"},"defaultLocalizedName":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.common.Geo"},"com.linkedin.deco.recipe.anonymous.Anon1251747613":{"fields":{"urn":{"type":"string"},"modelName":{"type":"string"},"fieldName":{"type":"string"},"value":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.common.StringFieldReference"},"com.linkedin.deco.recipe.anonymous.Anon1927941263":{"fields":{"entityUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.organization.Company"},"com.linkedin.voyager.dash.deco.common.image.ProfileWithoutFrame":{"fields":{"profilePicture":{"type":"com.linkedin.voyager.dash.deco.common.image.PhotoFilterPicture"},"entityUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.identity.profile.Profile"},"com.linkedin.deco.recipe.anonymous.Anon587401631":{"fields":{"entityUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.identity.profile.Profile"},"com.linkedin.voyager.dash.deco.common.text.OrganizationalPage":{"fields":{"entityUrn":{"type":"string"},"localizedName":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.organization.OrganizationalPage"},"com.linkedin.deco.recipe.anonymous.Anon1869367056":{"fields":{"entityUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.groups.Group"},"com.linkedin.deco.recipe.anonymous.Anon462674420":{"fields":{"actionTarget":{"type":"string"},"entityUrn":{"type":"string"},"displayName":{"type":"string"},"trackingUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.feed.Hashtag"},"com.linkedin.deco.recipe.anonymous.Anon1031101697":{"fields":{"targetInviteeResolutionResult":{"type":"com.linkedin.voyager.dash.deco.relationships.ProfileWithEmailRequired","resolvedFrom":"targetInvitee"},"inviter":{"type":"string"},"targetInvitee":{"type":"string"},"invitationRelationshipForm":{"type":"com.linkedin.deco.recipe.anonymous.Anon918376989"},"inviterResolutionResult":{"type":"com.linkedin.voyager.dash.deco.relationships.ProfileWithIweWarned","resolvedFrom":"inviter"}},"baseType":"com.linkedin.voyager.dash.relationships.invitation.NoInvitation"},"com.linkedin.voyager.dash.deco.identity.profile.WebTopCardCore":{"fields":{"birthDateOn":{"type":"com.linkedin.voyager.dash.deco.common.Date"},"lastName":{"type":"string"},"memorialized":{"type":"boolean"},"objectUrn":{"type":"string"},"multiLocaleLastName":{"type":{"map":"string"}},"showPremiumSubscriberBadge":{"type":"boolean"},"tempStatusEmoji":{"type":"string"},"pronounUnion":{"type":{"union":{"customPronoun":"string","standardizedPronoun":"string"}}},"tempStatusExpiredAtUnion":{"type":{"union":{"customizedExpiredAt":"long","standardizedExpiration":"string"}}},"multiLocaleFirstName":{"type":{"map":"string"}},"premium":{"type":"boolean"},"influencer":{"type":"boolean"},"entityUrn":{"type":"string"},"multiLocaleTempStatus":{"type":{"map":"string"}},"experienceCardUrn":{"type":"string"},"headlineGeneratedSuggestionDelegateUrn":{"type":"string"},"experienceCard":{"type":"com.linkedin.deco.recipe.anonymous.Anon1052602939","resolvedFrom":"experienceCardUrn"},"headline":{"type":"string"},"publicIdentifier":{"type":"string"},"topVoiceBadge":{"type":"com.linkedin.deco.recipe.anonymous.Anon1247784858"},"trackingId":{"type":"string"},"creator":{"type":"boolean"},"supportedLocales":{"type":{"array":"com.linkedin.voyager.dash.deco.common.Locale"}},"educationCard":{"type":"com.linkedin.deco.recipe.anonymous.Anon1052602939","resolvedFrom":"educationCardUrn"},"creatorInfo":{"type":"com.linkedin.deco.recipe.anonymous.Anon1140274151"},"versionTag":{"type":"string"},"privacySettings":{"type":"com.linkedin.voyager.dash.deco.identity.profile.ViewerPrivacySettingsForInjection","isInjection":true},"firstName":{"type":"string"},"profilePicture":{"type":"com.linkedin.voyager.dash.deco.identity.profile.ProfilePhotoDecoSpecEditableProfilePicture"},"geoLocation":{"type":"com.linkedin.deco.recipe.anonymous.Anon2049076601"},"multiLocaleMaidenName":{"type":{"map":"string"}},"tempStatus":{"type":"string"},"memberRelationship":{"type":"com.linkedin.voyager.dash.deco.relationships.MemberRelationshipV2ForInjection","isInjection":true},"profileGeneratedSuggestionPromo":{"type":"com.linkedin.deco.recipe.anonymous.Anon1967775378","isInjection":true},"multiLocaleHeadline":{"type":{"map":"string"}},"primaryLocale":{"type":"com.linkedin.voyager.dash.deco.common.LocaleFull"},"educationCardUrn":{"type":"string"},"backgroundPicture":{"type":"com.linkedin.voyager.dash.deco.identity.profile.ProfilePhotoDecoSpecEditableBackgroundPicture"}},"baseType":"com.linkedin.voyager.dash.identity.profile.Profile"},"com.linkedin.deco.recipe.anonymous.Anon1320789737":{"fields":{"ringContentType":{"type":"string"},"actionTarget":{"type":"string"},"preDashEntityUrn":{"type":"string"},"entityUrn":{"type":"string"},"emphasized":{"type":"boolean"}},"baseType":"com.linkedin.voyager.dash.common.image.RingStatus"},"com.linkedin.deco.recipe.anonymous.Anon163061530":{"fields":{"name":{"type":"string"},"entityUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.groups.Group"},"com.linkedin.deco.recipe.anonymous.Anon1568806612":{"fields":{"school":{"type":"com.linkedin.deco.recipe.anonymous.Anon929195650","resolvedFrom":"schoolUrn"},"vectorImage":{"type":"com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrlAndAttribution"},"schoolUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.common.image.NonEntitySchoolLogo"},"com.linkedin.voyager.dash.deco.common.text.ProfileForFullName":{"fields":{"lastName":{"type":"string"},"firstName":{"type":"string"},"entityUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.identity.profile.Profile"},"com.linkedin.voyager.dash.deco.common.image.Profile":{"fields":{"profilePicture":{"type":"com.linkedin.voyager.dash.deco.common.image.PhotoFilterPicture"},"entityUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.identity.profile.Profile"},"com.linkedin.voyager.dash.deco.common.text.JobPosting":{"fields":{"title":{"type":"string"},"entityUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.jobs.JobPosting"},"com.linkedin.voyager.dash.deco.relationships.MemberRelationshipV2ForInjection":{"fields":{"memberRelationshipData":{"type":{"union":{"noInvitation":"com.linkedin.deco.recipe.anonymous.Anon1031101697","invitation":"com.linkedin.voyager.dash.deco.relationships.Invitation","connection":"com.linkedin.voyager.dash.deco.relationships.Connection"}}},"entityUrn":{"type":"string"},"memberRelationshipUnion":{"type":{"union":{"self":"com.linkedin.restli.common.EmptyRecord","connection":"com.linkedin.voyager.dash.deco.relationships.Connection","noConnection":"com.linkedin.voyager.dash.deco.relationships.NoConnection"}}}},"baseType":"com.linkedin.voyager.dash.relationships.MemberRelationship"},"com.linkedin.voyager.dash.deco.relationships.ProfileWithIweWarned":{"fields":{"memorialized":{"type":"boolean"},"lastName":{"type":"string"},"firstName":{"type":"string"},"tempStatus":{"type":"string"},"entityUrn":{"type":"string"},"tempStatusEmoji":{"type":"string"},"iweWarned":{"type":"boolean"},"publicIdentifier":{"type":"string"},"headline":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.identity.profile.Profile"},"com.linkedin.voyager.dash.deco.common.LocaleFull":{"fields":{"variant":{"type":"string"},"country":{"type":"string"},"language":{"type":"string"},"extensions":{"type":"com.linkedin.voyager.dash.deco.common.LocaleExtensionsFull"},"script":{"type":"string"}},"baseType":"com.linkedin.common.Locale"},"com.linkedin.voyager.dash.deco.identity.profile.ViewerPrivacySettingsForInjection":{"fields":{"fullLastNameShown":{"type":"boolean"},"requireReferral":{"type":"boolean"},"showPublicProfile":{"type":"boolean"},"formerNameVisibilitySetting":{"type":"string"},"messagingSeenReceipts":{"type":"string"},"discloseAsProfileViewer":{"type":"string"},"allowProfileEditBroadcasts":{"type":"boolean"},"messagingTypingIndicators":{"type":"string"},"allowOpenProfile":{"type":"boolean"},"profilePictureVisibilitySetting":{"type":"string"},"entityUrn":{"type":"string"},"publicProfilePictureVisibilitySetting":{"type":"string"},"namePronunciationVisibilitySetting":{"type":"string"},"pronounVisibilitySetting":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.identity.profile.PrivacySettings"},"com.linkedin.voyager.dash.deco.common.image.ImageViewModel":{"fields":{"attributes":{"type":{"array":"com.linkedin.voyager.dash.deco.common.image.ImageAttribute"}},"actionTarget":{"type":"string"},"totalCount":{"type":"int"},"accessibilityTextAttributes":{"type":{"array":"com.linkedin.voyager.dash.deco.common.text.TextAttributeV2"}},"accessibilityText":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.common.image.ImageViewModel"},"com.linkedin.voyager.dash.deco.common.text.TextAttributeV2":{"fields":{"start":{"type":"int"},"length":{"type":"int"},"detailData":{"type":{"union":{"jobPostingName":"com.linkedin.voyager.dash.deco.common.text.JobPosting","profileFamiliarName":"com.linkedin.voyager.dash.deco.common.text.ProfileForFamiliarName","groupName":"com.linkedin.deco.recipe.anonymous.Anon163061530","profileFullName":"com.linkedin.voyager.dash.deco.common.text.ProfileForFullName","learningCourseName":"com.linkedin.voyager.dash.deco.common.text.LearningCourse","companyName":"com.linkedin.voyager.dash.deco.common.text.Company","profileMention":"com.linkedin.voyager.dash.deco.common.text.ProfileForMention","schoolName":"com.linkedin.voyager.dash.deco.common.text.School","organizationalPageName":"com.linkedin.voyager.dash.deco.common.text.OrganizationalPage","hashtag":"com.linkedin.voyager.dash.deco.common.text.Hashtag"}},"resolvedFrom":"detailDataUnion"},"detailDataUnion":{"type":{"union":{"jobPostingName":"string","profileFamiliarName":"string","hyperlink":"string","color":"string","companyName":"string","icon":"string","systemImage":"string","epoch":"com.linkedin.deco.recipe.anonymous.Anon858976209","organizationalPageName":"string","textLink":"com.linkedin.deco.recipe.anonymous.Anon1465360068","listItemStyle":"com.linkedin.deco.recipe.anonymous.Anon409680083","hyperlinkOpenExternally":"string","listStyle":"string","groupName":"string","profileFullName":"string","stringFieldReference":"com.linkedin.deco.recipe.anonymous.Anon1251747613","learningCourseName":"string","profileMention":"string","style":"string","schoolName":"string","hashtag":"string"}}}},"baseType":"com.linkedin.voyager.dash.common.text.TextAttribute"},"com.linkedin.deco.recipe.anonymous.Anon648914460":{"fields":{"companyUrn":{"type":"string"},"company":{"type":"com.linkedin.deco.recipe.anonymous.Anon1927941263","resolvedFrom":"companyUrn"},"vectorImage":{"type":"com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrlAndAttribution"}},"baseType":"com.linkedin.voyager.dash.common.image.NonEntityCompanyLogo"},"com.linkedin.voyager.dash.deco.relationships.NoConnection":{"fields":{"memberDistance":{"type":"string"},"invitationUnion":{"type":{"union":{"noInvitation":"com.linkedin.deco.recipe.anonymous.Anon1031101697","invitation":"com.linkedin.voyager.dash.deco.relationships.Invitation"}}}},"baseType":"com.linkedin.voyager.dash.relationships.NoConnection"},"com.linkedin.voyager.dash.deco.common.text.ProfileForMention":{"fields":{"entityUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.identity.profile.Profile"},"com.linkedin.deco.recipe.anonymous.Anon1052602939":{"fields":{"entityUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.identity.profile.tetris.Card"},"com.linkedin.voyager.dash.deco.common.text.Hashtag":{"fields":{"entityUrn":{"type":"string"},"trackingUrn":{"type":"string"},"actionTarget":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.feed.Hashtag"},"com.linkedin.deco.recipe.anonymous.Anon1465360068":{"fields":{"viewingBehavior":{"type":"string"},"url":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.common.text.TextLink"},"com.linkedin.deco.recipe.anonymous.Anon1528523240":{"fields":{"controlName":{"type":"string"},"accessibilityText":{"type":"string"},"appearance":{"type":"com.linkedin.voyager.dash.deco.common.ux.ButtonAppearance"}},"baseType":"com.linkedin.voyager.dash.identity.profile.ProfileGeneratedSuggestionButton"},"com.linkedin.deco.recipe.anonymous.Anon2049076601":{"fields":{"geo":{"type":"com.linkedin.deco.recipe.anonymous.Anon1745422644","resolvedFrom":"geoUrn"},"geoUrn":{"type":"string"},"postalCode":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.identity.profile.ProfileGeoLocation"},"com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrlAndAttribution":{"fields":{"attribution":{"type":"string"},"rootUrl":{"type":"string"},"artifacts":{"type":{"array":"com.linkedin.voyager.dash.deco.common.VectorArtifact"}}},"baseType":"com.linkedin.common.VectorImage"},"com.linkedin.voyager.dash.deco.common.FullPaging":{"fields":{"start":{"type":"int"},"count":{"type":"int"},"total":{"type":"int"},"links":{"type":{"array":"com.linkedin.voyager.dash.deco.common.Link"}}},"baseType":"com.linkedin.restli.common.CollectionMetadata"},"com.linkedin.voyager.dash.deco.common.image.ProfessionalEvent":{"fields":{"logoImage":{"type":{"union":{"url":"string","vectorImage":"com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrlAndAttribution"}}},"entityUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.events.ProfessionalEvent"},"com.linkedin.deco.recipe.anonymous.Anon336652209":{"fields":{"profilePicture":{"type":"com.linkedin.voyager.dash.deco.identity.profile.ProfilePhotoDecoSpecReadOnlyProfilePicture"},"memorialized":{"type":"boolean"},"lastName":{"type":"string"},"firstName":{"type":"string"},"tempStatus":{"type":"string"},"entityUrn":{"type":"string"},"tempStatusEmoji":{"type":"string"},"publicIdentifier":{"type":"string"},"headline":{"type":"string"},"tempStatusExpiredAtUnion":{"type":{"union":{"customizedExpiredAt":"long","standardizedExpiration":"string"}}}},"baseType":"com.linkedin.voyager.dash.identity.profile.Profile"},"com.linkedin.deco.recipe.anonymous.Anon1436383648":{"fields":{"groupUrn":{"type":"string"},"vectorImage":{"type":"com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrlAndAttribution"},"group":{"type":"com.linkedin.deco.recipe.anonymous.Anon1869367056","resolvedFrom":"groupUrn"}},"baseType":"com.linkedin.voyager.dash.common.image.NonEntityGroupLogo"},"com.linkedin.voyager.dash.deco.common.VectorArtifact":{"fields":{"width":{"type":"int"},"fileIdentifyingUrlPathSegment":{"type":"string"},"expiresAt":{"type":"long"},"height":{"type":"int"}},"baseType":"com.linkedin.common.VectorArtifact"},"com.linkedin.voyager.dash.deco.common.text.School":{"fields":{"name":{"type":"string"},"entityUrn":{"type":"string"}},"baseType":"com.linkedin.voyager.dash.organization.School"},"com.linkedin.voyager.dash.deco.common.Date":{"fields":{"month":{"type":"int"},"year":{"type":"int"},"day":{"type":"int"}},"baseType":"com.linkedin.common.Date"}}}},"included":[{"paging":{"start":0,"count":10,"links":[],"$recipeTypes":["com.linkedin.voyager.dash.deco.common.FullPaging"],"$type":"com.linkedin.restli.common.CollectionMetadata"},"entityUrn":"urn:li:collectionResponse:C+plF+jAW9RWodokwpxA11PGGFAi5Lv3OuHf5wFgdvA=","$recipeTypes":["com.linkedin.deco.recipe.anonymous.Anon1967775378"],"elements":[],"$type":"com.linkedin.restli.common.CollectionResponse"},{"entityUrn":"urn:li:fsd_geo:101165590","$recipeTypes":["com.linkedin.deco.recipe.anonymous.Anon1918694303"],"defaultLocalizedName":"United Kingdom","$type":"com.linkedin.voyager.dash.common.Geo"},{"countryUrn":"urn:li:fsd_geo:101165590","defaultLocalizedNameWithoutCountryName":"Leeds, England","*country":"urn:li:fsd_geo:101165590","entityUrn":"urn:li:fsd_geo:102943586","$recipeTypes":["com.linkedin.deco.recipe.anonymous.Anon1745422644"],"defaultLocalizedName":"Leeds, England, United Kingdom","$type":"com.linkedin.voyager.dash.common.Geo"},{"fullLastNameShown":true,"showPremiumSubscriberBadge":null,"formerNameVisibilitySetting":"CONNECTIONS","discloseAsProfileViewer":"DISCLOSE_FULL","messagingSeenReceipts":null,"allowProfileEditBroadcasts":null,"messagingTypingIndicators":null,"entityUrn":"urn:li:fsd_privacySettings:singleton","publicProfilePictureVisibilitySetting":"PUBLIC","pronounVisibilitySetting":"MEMBERS","requireReferral":null,"showPublicProfile":true,"$recipeTypes":["com.linkedin.voyager.dash.deco.identity.profile.ViewerPrivacySettingsForInjection"],"$type":"com.linkedin.voyager.dash.identity.profile.PrivacySettings","allowOpenProfile":false,"profilePictureVisibilitySetting":"PUBLIC","namePronunciationVisibilitySetting":"MEMBERS"},{"birthDateOn":{"month":3,"day":6,"$recipeTypes":["com.linkedin.voyager.dash.deco.common.Date"],"$type":"com.linkedin.common.Date"},"objectUrn":"urn:li:member:793767623","multiLocaleLastName":{"en_US":"Al-Safi"},"$anti_abuse_metadata":{"/phoneticFirstName":{"sourceUrns":{"com.linkedin.common.urn.MemberUrn":"urn:li:member:793767623"}},"/headlineGeneratedSuggestionDelegateUrn":{"sourceUrns":{"com.linkedin.common.urn.MemberUrn":"urn:li:member:793767623"}},"/industryV2Urn":{"sourceUrns":{"com.linkedin.common.urn.MemberUrn":"urn:li:member:793767623"}},"/tempStatus":{"sourceUrns":{"com.linkedin.common.urn.MemberUrn":"urn:li:member:793767623"}},"/defaultToActivityTab":{"sourceUrns":{"com.linkedin.common.urn.MemberUrn":"urn:li:member:793767623"}},"/companyNameOnProfileTopCardShown":{"sourceUrns":{"com.linkedin.common.urn.MemberUrn":"urn:li:member:793767623"}},"/summary":{"sourceUrns":{"com.linkedin.common.urn.MemberUrn":"urn:li:member:793767623"}},"/influencer":{"sourceUrns":{"com.linkedin.common.urn.MemberUrn":"urn:li:member:793767623"}},"/trackingId":{"sourceUrns":{"com.linkedin.common.urn.MemberUrn":"urn:li:member:793767623"}},"/address":{"sourceUrns":{"com.linkedin.common.urn.MemberUrn":"urn:li:member:793767623"}},"/objectUrn":{"sourceUrns":{"com.linkedin.common.urn.MemberUrn":"urn:li:member:793767623"}},"/emailRequired":{"sourceUrns":{"com.linkedin.common.urn.MemberUrn":"urn:li:member:793767623"}},"/geoLocationBackfilled":{"sourceUrns":{"com.linkedin.common.urn.MemberUrn":"urn:li:member:793767623"}},"/versionTag":{"sourceUrns":{"com.linkedin.common.urn.MemberUrn":"urn:li:member:793767623"}},"/premium":{"sourceUrns":{"com.linkedin.common.urn.MemberUrn":"urn:li:member:793767623"}},"/headline":{"sourceUrns":{"com.linkedin.common.urn.MemberUrn":"urn:li:member:793767623"}},"/showPremiumSubscriberBadge":{"sourceUrns":{"com.linkedin.common.urn.MemberUrn":"urn:li:member:793767623"}},"/educationCardUrn":{"sourceUrns":{"com.linkedin.common.urn.MemberUrn":"urn:li:member:793767623"}},"/experienceCardUrn":{"sourceUrns":{"com.linkedin.common.urn.MemberUrn":"urn:li:member:793767623"}},"/locationName":{"sourceUrns":{"com.linkedin.common.urn.MemberUrn":"urn:li:member:793767623"}},"/industryUrn":{"sourceUrns":{"com.linkedin.common.urn.MemberUrn":"urn:li:member:793767623"}},"/educationOnProfileTopCardShown":{"sourceUrns":{"com.linkedin.common.urn.MemberUrn":"urn:li:member:793767623"}},"/trackingMemberId":{"sourceUrns":{"com.linkedin.common.urn.MemberUrn":"urn:li:member:793767623"}},"/lastName":{"sourceUrns":{"com.linkedin.common.urn.MemberUrn":"urn:li:member:793767623"}},"/memorialized":{"sourceUrns":{"com.linkedin.common.urn.MemberUrn":"urn:li:member:793767623"}},"/tempStatusEmoji":{"sourceUrns":{"com.linkedin.common.urn.MemberUrn":"urn:li:member:793767623"}},"/entityUrn":{"sourceUrns":{"com.linkedin.common.urn.MemberUrn":"urn:li:member:793767623"}},"/lastNamePronunciationHint":{"sourceUrns":{"com.linkedin.common.urn.MemberUrn":"urn:li:member:793767623"}},"/firstName":{"sourceUrns":{"com.linkedin.common.urn.MemberUrn":"urn:li:member:793767623"}},"/firstNamePronunciationHint":{"sourceUrns":{"com.linkedin.common.urn.MemberUrn":"urn:li:member:793767623"}},"/phoneticLastName":{"sourceUrns":{"com.linkedin.common.urn.MemberUrn":"urn:li:member:793767623"}},"/endorsementsEnabled":{"sourceUrns":{"com.linkedin.common.urn.MemberUrn":"urn:li:member:793767623"}},"/maidenName":{"sourceUrns":{"com.linkedin.common.urn.MemberUrn":"urn:li:member:793767623"}},"/creator":{"sourceUrns":{"com.linkedin.common.urn.MemberUrn":"urn:li:member:793767623"}},"/student":{"sourceUrns":{"com.linkedin.common.urn.MemberUrn":"urn:li:member:793767623"}},"/iweWarned":{"sourceUrns":{"com.linkedin.common.urn.MemberUrn":"urn:li:member:793767623"}},"/imFollowsPromoLegoTrackingId":{"sourceUrns":{"com.linkedin.common.urn.MemberUrn":"urn:li:member:793767623"}},"/publicIdentifier":{"sourceUrns":{"com.linkedin.common.urn.MemberUrn":"urn:li:member:793767623"}}},"pronounUnion":null,"*educationCard":"urn:li:fsd_profileCard:(ACoAAC9P7scB1yv1hA-ZjtKBAxcuNQvmvu08uhI,EDUCATION,en_US)","tempStatusExpiredAtUnion":null,"multiLocaleFirstName":{"en_US":"Harith"},"multiLocaleTempStatus":null,"experienceCardUrn":"urn:li:fsd_profileCard:(ACoAAC9P7scB1yv1hA-ZjtKBAxcuNQvmvu08uhI,EXPERIENCE,en_US)","headlineGeneratedSuggestionDelegateUrn":"urn:li:fsu_profileActionDelegate:112590533","publicIdentifier":"harith-al-safi","trackingId":"KanjSvd9RYCRhqUu+vTGKA==","topVoiceBadge":null,"*memberRelationship":"urn:li:fsd_memberRelationship:ACoAAC9P7scB1yv1hA-ZjtKBAxcuNQvmvu08uhI","versionTag":"3252161322","firstName":"Harith","profilePicture":{"$recipeTypes":["com.linkedin.voyager.dash.deco.identity.profile.ProfilePhotoDecoSpecEditableProfilePicture"],"photoFilterEditInfo":{"bottomLeft":{"x":0.09892999750081799,"y":0.795059979915095,"$recipeTypes":["com.linkedin.voyager.dash.deco.common.Coordinate2DFull"],"$type":"com.linkedin.common.Coordinate2D"},"vignette":0.0,"bottomRight":{"x":0.8398399787838571,"y":0.795059979915095,"$recipeTypes":["com.linkedin.voyager.dash.deco.common.Coordinate2DFull"],"$type":"com.linkedin.common.Coordinate2D"},"topRight":{"x":0.8398399787838571,"y":0.23938999395249994,"$recipeTypes":["com.linkedin.voyager.dash.deco.common.Coordinate2DFull"],"$type":"com.linkedin.common.Coordinate2D"},"$recipeTypes":["com.linkedin.deco.recipe.anonymous.Anon1309211116"],"$type":"com.linkedin.voyager.dash.identity.profile.PhotoFilterEditInfo","saturation":0.0,"brightness":0.0,"photoFilterType":"ORIGINAL","contrast":0.0,"topLeft":{"x":0.09892999750081799,"y":0.23938999395249994,"$recipeTypes":["com.linkedin.voyager.dash.deco.common.Coordinate2DFull"],"$type":"com.linkedin.common.Coordinate2D"}},"$type":"com.linkedin.voyager.dash.identity.profile.PhotoFilterPicture","originalImageReference":{"vectorImage":{"$recipeTypes":["com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrlAndAttribution"],"rootUrl":"https://www.linkedin.com/dms/D4E04AQF9WlDEmiHFSQ/profile-originalphoto-shrink_","artifacts":[{"width":675,"$recipeTypes":["com.linkedin.voyager.dash.deco.common.VectorArtifact"],"fileIdentifyingUrlPathSegment":"900_1200/0/1675373177230?m=AQIQknf-ESwlhwAAAYidBvuENz6caSs-K0jspAnDdHZVteJIw2G17sbJyA&amp;e=1686348060&amp;v=beta&amp;t=fYbf6gaer4m6OaGUV3q6q3fn2-NMC32FE8DouHVvgSw","expiresAt":1686348060000,"height":900,"$type":"com.linkedin.common.VectorArtifact"},{"width":337,"$recipeTypes":["com.linkedin.voyager.dash.deco.common.VectorArtifact"],"fileIdentifyingUrlPathSegment":"450_600/0/1675373177230?m=AQKGwPYUGQhFEAAAAYidBvuEzzFnlH7BQ9Jr7o1_ukaKBrvfwoYI2jQJXA&amp;e=1686348060&amp;v=beta&amp;t=_FOJcquxXFrsEGsTJNMAWq9PHM_VHcBorBtstwfDHdY","expiresAt":1686348060000,"height":450,"$type":"com.linkedin.common.VectorArtifact"}],"$type":"com.linkedin.common.VectorImage"}},"originalImageUrn":"urn:li:digitalmediaAsset:D4E04AQF9WlDEmiHFSQ","a11yText":"Harith Al-Safi","displayImageReference":{"vectorImage":{"$recipeTypes":["com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrlAndAttribution"],"rootUrl":"https://media.licdn.com/dms/image/D4E03AQGB3OP3rlsmtQ/profile-displayphoto-shrink_","artifacts":[{"width":100,"$recipeTypes":["com.linkedin.voyager.dash.deco.common.VectorArtifact"],"fileIdentifyingUrlPathSegment":"100_100/0/1675373176223?e=1691625600&amp;v=beta&amp;t=-3k4RuOJvA8N9zuEKPE4wNyFxg7L6jKBLgCDUEe33ec","expiresAt":1691625600000,"height":100,"$type":"com.linkedin.common.VectorArtifact"},{"width":200,"$recipeTypes":["com.linkedin.voyager.dash.deco.common.VectorArtifact"],"fileIdentifyingUrlPathSegment":"200_200/0/1675373176223?e=1691625600&amp;v=beta&amp;t=_9o-z2z8w540NQAt4gMeniczzyyKkD0PQPcIiPgetgo","expiresAt":1691625600000,"height":200,"$type":"com.linkedin.common.VectorArtifact"},{"width":400,"$recipeTypes":["com.linkedin.voyager.dash.deco.common.VectorArtifact"],"fileIdentifyingUrlPathSegment":"400_400/0/1675373176223?e=1691625600&amp;v=beta&amp;t=OfegiYnmbSi2ez4L2Z9exoHtI1j77ximISKDtpMfBeM","expiresAt":1691625600000,"height":400,"$type":"com.linkedin.common.VectorArtifact"},{"width":800,"$recipeTypes":["com.linkedin.voyager.dash.deco.common.VectorArtifact"],"fileIdentifyingUrlPathSegment":"800_800/0/1675373176223?e=1691625600&amp;v=beta&amp;t=m1XIXW9S_uGc_fY4J_eZopCMpeJbO484Aha0oGVAeY8","expiresAt":1691625600000,"height":800,"$type":"com.linkedin.common.VectorArtifact"}],"$type":"com.linkedin.common.VectorImage"}},"displayImageUrn":"urn:li:digitalmediaAsset:D4E03AQGB3OP3rlsmtQ"},"multiLocaleMaidenName":null,"*profileGeneratedSuggestionPromo":"urn:li:collectionResponse:C+plF+jAW9RWodokwpxA11PGGFAi5Lv3OuHf5wFgdvA=","multiLocaleHeadline":{"en_US":"Software Engineer | Computer Engineer | AI Enthusiast "},"lastName":"Al-Safi","memorialized":false,"*experienceCard":"urn:li:fsd_profileCard:(ACoAAC9P7scB1yv1hA-ZjtKBAxcuNQvmvu08uhI,EXPERIENCE,en_US)","showPremiumSubscriberBadge":false,"tempStatusEmoji":null,"premium":false,"influencer":false,"entityUrn":"urn:li:fsd_profile:ACoAAC9P7scB1yv1hA-ZjtKBAxcuNQvmvu08uhI","headline":"Software Engineer | Computer Engineer | AI Enthusiast ","creator":false,"supportedLocales":[{"country":"US","language":"en","$recipeTypes":["com.linkedin.voyager.dash.deco.common.Locale"],"$type":"com.linkedin.common.Locale"}],"creatorInfo":null,"$recipeTypes":["com.linkedin.voyager.dash.deco.identity.profile.WebTopCardCore"],"$type":"com.linkedin.voyager.dash.identity.profile.Profile","geoLocation":{"*geo":"urn:li:fsd_geo:102943586","$recipeTypes":["com.linkedin.deco.recipe.anonymous.Anon2049076601"],"geoUrn":"urn:li:fsd_geo:102943586","postalCode":"LS71AW","$type":"com.linkedin.voyager.dash.identity.profile.ProfileGeoLocation"},"*privacySettings":"urn:li:fsd_privacySettings:singleton","tempStatus":null,"primaryLocale":{"country":"US","language":"en","$recipeTypes":["com.linkedin.voyager.dash.deco.common.LocaleFull"],"$type":"com.linkedin.common.Locale"},"backgroundPicture":{"originalImageReference":{"vectorImage":{"$recipeTypes":["com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrlAndAttribution"],"rootUrl":"https://www.linkedin.com/dms/C4E04AQEYtps-6Ucpew/profile-originalbackgroundimage-shrink_","artifacts":[{"width":924,"$recipeTypes":["com.linkedin.voyager.dash.deco.common.VectorArtifact"],"fileIdentifyingUrlPathSegment":"396_1584/0/1619145014780?m=AQKSrqu3zMejaQAAAYidBvuFXiVrCT_swmGCWklsjz4O901yIfn3lz7k5A&amp;e=1686348060&amp;v=beta&amp;t=fEOurifJcUMHmeVCwFf-PP3EmnLzsdxca4mLqj4TsUg","expiresAt":1686348060000,"height":396,"$type":"com.linkedin.common.VectorArtifact"},{"width":466,"$recipeTypes":["com.linkedin.voyager.dash.deco.common.VectorArtifact"],"fileIdentifyingUrlPathSegment":"200_800/0/1619145014780?m=AQLmEfBIEfUGkQAAAYidBvuFq78V2DCz0YBUc_ASr6pQ2F79O4bORmkZmg&amp;e=1686348060&amp;v=beta&amp;t=XM5dA-0OLBrJ1_gObRQaIec8Z-CSNn48hNlbdGxQgSs","expiresAt":1686348060000,"height":200,"$type":"com.linkedin.common.VectorArtifact"}],"$type":"com.linkedin.common.VectorImage"}},"originalImageUrn":"urn:li:digitalmediaAsset:C4E04AQEYtps-6Ucpew","displayImageReference":{"vectorImage":{"$recipeTypes":["com.linkedin.voyager.dash.deco.common.VectorImageOnlyRootUrlAndAttribution"],"rootUrl":"https://media.licdn.com/dms/image/C4E16AQHpKX8W_8U4dQ/profile-displaybackgroundimage-shrink_","artifacts":[{"width":800,"$recipeTypes":["com.linkedin.voyager.dash.deco.common.VectorArtifact"],"fileIdentifyingUrlPathSegment":"200_800/0/1619145014133?e=1691625600&amp;v=beta&amp;t=WNJVHkD-IOqS7Cro0mPXbkkXcylhyc4XywGf7-ZVYRs","expiresAt":1691625600000,"height":200,"$type":"com.linkedin.common.VectorArtifact"},{"width":1400,"$recipeTypes":["com.linkedin.voyager.dash.deco.common.VectorArtifact"],"fileIdentifyingUrlPathSegment":"350_1400/0/1619145014133?e=1691625600&amp;v=beta&amp;t=CCLM2DPbxKAIxgLF76CdQ1Gp-FUJMQmjz1DQmsMOOfU","expiresAt":1691625600000,"height":350,"$type":"com.linkedin.common.VectorArtifact"}],"$type":"com.linkedin.common.VectorImage"}},"$recipeTypes":["com.linkedin.voyager.dash.deco.identity.profile.ProfilePhotoDecoSpecEditableBackgroundPicture"],"displayImageUrn":"urn:li:digitalmediaAsset:C4E16AQHpKX8W_8U4dQ","photoFilterEditInfo":{"bottomLeft":{"x":8.167157882300002E-17,"y":0.7818791946308725,"$recipeTypes":["com.linkedin.voyager.dash.deco.common.Coordinate2DFull"],"$type":"com.linkedin.common.Coordinate2D"},"vignette":0.0,"bottomRight":{"x":1.0,"y":0.7818791946308725,"$recipeTypes":["com.linkedin.voyager.dash.deco.common.Coordinate2DFull"],"$type":"com.linkedin.common.Coordinate2D"},"topRight":{"x":1.0,"y":0.1979865771812081,"$recipeTypes":["com.linkedin.voyager.dash.deco.common.Coordinate2DFull"],"$type":"com.linkedin.common.Coordinate2D"},"$recipeTypes":["com.linkedin.deco.recipe.anonymous.Anon1309211116"],"$type":"com.linkedin.voyager.dash.identity.profile.PhotoFilterEditInfo","saturation":0.0,"brightness":0.0,"photoFilterType":"ORIGINAL","contrast":0.0,"topLeft":{"x":8.167157882300002E-17,"y":0.1979865771812081,"$recipeTypes":["com.linkedin.voyager.dash.deco.common.Coordinate2DFull"],"$type":"com.linkedin.common.Coordinate2D"}},"$type":"com.linkedin.voyager.dash.identity.profile.PhotoFilterPicture"},"educationCardUrn":"urn:li:fsd_profileCard:(ACoAAC9P7scB1yv1hA-ZjtKBAxcuNQvmvu08uhI,EDUCATION,en_US)"},{"entityUrn":"urn:li:fsd_profileCard:(ACoAAC9P7scB1yv1hA-ZjtKBAxcuNQvmvu08uhI,EXPERIENCE,en_US)","$recipeTypes":["com.linkedin.deco.recipe.anonymous.Anon1052602939"],"$type":"com.linkedin.voyager.dash.identity.profile.tetris.Card"},{"entityUrn":"urn:li:fsd_profileCard:(ACoAAC9P7scB1yv1hA-ZjtKBAxcuNQvmvu08uhI,EDUCATION,en_US)","$recipeTypes":["com.linkedin.deco.recipe.anonymous.Anon1052602939"],"$type":"com.linkedin.voyager.dash.identity.profile.tetris.Card"},{"memberRelationshipUnion":{"self":{"$type":"com.linkedin.restli.common.EmptyRecord"}},"entityUrn":"urn:li:fsd_memberRelationship:ACoAAC9P7scB1yv1hA-ZjtKBAxcuNQvmvu08uhI","$recipeTypes":["com.linkedin.voyager.dash.deco.relationships.MemberRelationshipV2ForInjection"],"memberRelationshipData":null,"$type":"com.linkedin.voyager.dash.relationships.MemberRelationship"}]}
</code>



  <svg aria-hidden="true" role="none" xmlns="http://www.w3.org/2000/svg" id="hue-web-icons-sprite" style="display: none;">
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" id="caret-small" data-supported-dps="16x16" fill="currentColor">
  <path d="M8 11L3 6h10z" fill-rule="evenodd"></path>
</svg>

    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" id="overflow-web-ios-small" data-supported-dps="16x16" fill="currentColor">
  <path d="M3 9.5A1.5 1.5 0 114.5 8 1.5 1.5 0 013 9.5zM11.5 8A1.5 1.5 0 1013 6.5 1.5 1.5 0 0011.5 8zm-5 0A1.5 1.5 0 108 6.5 1.5 1.5 0 006.5 8z"></path>
</svg>

    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" id="search-small" data-supported-dps="16x16" fill="currentColor">
  <path d="M14.56 12.44L11.3 9.18a5.51 5.51 0 10-2.12 2.12l3.26 3.26a1.5 1.5 0 102.12-2.12zM3 6.5A3.5 3.5 0 116.5 10 3.5 3.5 0 013 6.5z"></path>
</svg>

</svg>

  <!---->

  <!---->

    <div id="artdeco-global-alert-container" class="ember-view"><!----><!----></div>

<div class="application-outlet">
<!---->
        <div class="global-nav__a11y-menu
    ">
  <div class="global-nav__a11y-menu-container">
      <button id="ember7" class="mr4 artdeco-button artdeco-button--muted artdeco-button--2 artdeco-button--secondary ember-view"><!---->
<span class="artdeco-button__text">
    Skip to search
</span></button>

    <button id="ember8" class="artdeco-button artdeco-button--muted artdeco-button--2 artdeco-button--secondary ember-view"><!---->
<span class="artdeco-button__text">
    Skip to main content
</span></button>

    <button id="ember9" class="global-nav__a11y-menu-close artdeco-button artdeco-button--circle artdeco-button--muted artdeco-button--2 artdeco-button--tertiary ember-view">  <li-icon aria-hidden="true" type="close" class="artdeco-button__icon"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-supported-dps="24x24" fill="currentColor" class="mercado-match" width="24" height="24" focusable="false">
  <path d="M13.42 12L20 18.58 18.58 20 12 13.42 5.42 20 4 18.58 10.58 12 4 5.42 5.42 4 12 10.58 18.58 4 20 5.42z"></path>
</svg></li-icon>

<span class="artdeco-button__text">
    Close jump menu
</span></button>
  </div>
</div>
      <header id="global-nav" class="global-nav global-alert-offset-top
    
    global-nav--visible">
  <div class="global-nav__content">
      <a class="app-aware-link " href="https://www.linkedin.com/feed/?nis=true" data-test-app-aware-link="">
    
    <div class="ivm-image-view-model    global-nav__branding-logo">
        
    <div class="ivm-view-attr__img-wrapper ivm-view-attr__img-wrapper--use-img-tag display-flex
        
        ">
        <li-icon type="app-linkedin-bug-color-icon" class=" " size="large" role="img" aria-label="LinkedIn"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-supported-dps="24x24" fill="currentColor" class="mercado-match" width="24" height="24" focusable="false">
  <path d="M20.5 2h-17A1.5 1.5 0 002 3.5v17A1.5 1.5 0 003.5 22h17a1.5 1.5 0 001.5-1.5v-17A1.5 1.5 0 0020.5 2zM8 19H5v-9h3zM6.5 8.25A1.75 1.75 0 118.3 6.5a1.78 1.78 0 01-1.8 1.75zM19 19h-3v-4.74c0-1.42-.6-1.93-1.38-1.93A1.74 1.74 0 0013 14.19a.66.66 0 000 .14V19h-3v-9h2.9v1.3a3.11 3.11 0 012.7-1.4c1.55 0 3.36.86 3.36 3.66z"></path>
</svg></li-icon>
    </div>
  
          </div>
  
</a>

    <div id="global-nav-search" class="global-nav__search
        ">
      
          <div class="search-global-typeahead
    
     global-nav__search-typeahead">
    <div id="global-nav-typeahead" class="search-global-typeahead__typeahead">
<!---->    
      <input class="search-global-typeahead__input" placeholder="Search" role="combobox" aria-autocomplete="list" aria-label="Search" aria-activedescendant="" aria-expanded="false" type="text">

      <div aria-hidden="true" class="search-global-typeahead__search-icon-container">
        <li-icon aria-hidden="true" type="search" class="search-global-typeahead__search-icon" size="small"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" data-supported-dps="16x16" fill="currentColor" class="mercado-match" width="16" height="16" focusable="false">
  <path d="M14.56 12.44L11.3 9.18a5.51 5.51 0 10-2.12 2.12l3.26 3.26a1.5 1.5 0 102.12-2.12zM3 6.5A3.5 3.5 0 116.5 10 3.5 3.5 0 013 6.5z"></path>
</svg></li-icon>
      </div>
<!---->      <div class="search-global-typeahead__overlay global-alert-offset-top
          "></div>
<!---->    
</div>
  <button class="search-global-typeahead__collapsed-search-button" aria-label="Click to start a search" type="button">
    <li-icon aria-hidden="true" type="search" class="search-global-typeahead__collapsed-search-button-icon t-black--light" size="medium"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-supported-dps="24x24" fill="currentColor" class="mercado-match" width="24" height="24" focusable="false">
  <path d="M21.41 18.59l-5.27-5.28A6.83 6.83 0 0017 10a7 7 0 10-7 7 6.83 6.83 0 003.31-.86l5.28 5.27a2 2 0 002.82-2.82zM5 10a5 5 0 115 5 5 5 0 01-5-5z"></path>
</svg></li-icon>
    <div class="search-global-typeahead__collapsed-search-button-text t-black--light t-12 t-normal">
      Search
    </div>
  </button>
  <div id="ember11" class="ember-view"><!----></div>
</div>
      
    </div>

    <nav class="global-nav__nav" aria-label="Primary Navigation">
      <ul class="global-nav__primary-items
          ">
          <li class="global-nav__primary-item
              ">
                <a class="app-aware-link  global-nav__primary-link" target="_self" href="https://www.linkedin.com/feed/?nis=true&amp;" data-test-app-aware-link="">
  
  <div id="ember12" class="global-nav__primary-link-notif artdeco-notification-badge ember-view">  <span class="notification-badge notification-badge--show ">
        <span aria-hidden="true" class="notification-badge__no-count"></span>
        <span class="a11y-text" data-test-notification-a11y="">new feed updates notifications</span>
  </span>
  
    
    <div class="ivm-image-view-model    global-nav__icon-ivm
        ">
        
    <div class="ivm-view-attr__img-wrapper ivm-view-attr__img-wrapper--use-img-tag display-flex
        
        ">
        <li-icon aria-hidden="true" type="home" class=" " size="large"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-supported-dps="24x24" fill="currentColor" class="mercado-match" width="24" height="24" focusable="false">
  <path d="M23 9v2h-2v7a3 3 0 01-3 3h-4v-6h-4v6H6a3 3 0 01-3-3v-7H1V9l11-7z"></path>
</svg></li-icon>
    </div>
  
          </div>
  
  
</div>


  <span class="t-12 break-words block t-black--light t-normal
      global-nav__primary-link-text" title="Home">
    Home
  </span>
</a>

<!---->
<!----><!----><!---->          </li>
          <li class="global-nav__primary-item
              ">
                <a class="app-aware-link  global-nav__primary-link" target="_self" href="https://www.linkedin.com/mynetwork/?" data-test-app-aware-link="">
  
    
    <div class="ivm-image-view-model    global-nav__icon-ivm
        ">
        
    <div class="ivm-view-attr__img-wrapper ivm-view-attr__img-wrapper--use-img-tag display-flex
        
        ">
        <li-icon aria-hidden="true" type="people" class=" " size="large"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-supported-dps="24x24" fill="currentColor" class="mercado-match" width="24" height="24" focusable="false">
  <path d="M12 16v6H3v-6a3 3 0 013-3h3a3 3 0 013 3zm5.5-3A3.5 3.5 0 1014 9.5a3.5 3.5 0 003.5 3.5zm1 2h-2a2.5 2.5 0 00-2.5 2.5V22h7v-4.5a2.5 2.5 0 00-2.5-2.5zM7.5 2A4.5 4.5 0 1012 6.5 4.49 4.49 0 007.5 2z"></path>
</svg></li-icon>
    </div>
  
          </div>
  


  <span class="t-12 break-words block t-black--light t-normal
      global-nav__primary-link-text" title="My Network">
    My Network
  </span>
</a>

<!---->
<!----><!----><!---->          </li>
          <li class="global-nav__primary-item
              ">
                <a class="app-aware-link  global-nav__primary-link" target="_self" href="https://www.linkedin.com/jobs/?" data-test-app-aware-link="">
  
    
    <div class="ivm-image-view-model    global-nav__icon-ivm
        ">
        
    <div class="ivm-view-attr__img-wrapper ivm-view-attr__img-wrapper--use-img-tag display-flex
        
        ">
        <li-icon aria-hidden="true" type="job" class=" " size="large"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-supported-dps="24x24" fill="currentColor" class="mercado-match" width="24" height="24" focusable="false">
  <path d="M17 6V5a3 3 0 00-3-3h-4a3 3 0 00-3 3v1H2v4a3 3 0 003 3h14a3 3 0 003-3V6zM9 5a1 1 0 011-1h4a1 1 0 011 1v1H9zm10 9a4 4 0 003-1.38V17a3 3 0 01-3 3H5a3 3 0 01-3-3v-4.38A4 4 0 005 14z"></path>
</svg></li-icon>
    </div>
  
          </div>
  


  <span class="t-12 break-words block t-black--light t-normal
      global-nav__primary-link-text" title="Jobs">
    Jobs
  </span>
</a>

<!---->
<!----><!----><!---->          </li>
          <li class="global-nav__primary-item
              ">
                <a class="app-aware-link  global-nav__primary-link" target="_self" href="https://www.linkedin.com/messaging/?" data-test-app-aware-link="">
  
    
    <div class="ivm-image-view-model    global-nav__icon-ivm
        ">
        
    <div class="ivm-view-attr__img-wrapper ivm-view-attr__img-wrapper--use-img-tag display-flex
        
        ">
        <li-icon aria-hidden="true" type="nav-small-messaging-icon" class=" " size="large"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-supported-dps="24x24" fill="currentColor" class="mercado-match" width="24" height="24" focusable="false">
  <path d="M16 4H8a7 7 0 000 14h4v4l8.16-5.39A6.78 6.78 0 0023 11a7 7 0 00-7-7zm-8 8.25A1.25 1.25 0 119.25 11 1.25 1.25 0 018 12.25zm4 0A1.25 1.25 0 1113.25 11 1.25 1.25 0 0112 12.25zm4 0A1.25 1.25 0 1117.25 11 1.25 1.25 0 0116 12.25z"></path>
</svg></li-icon>
    </div>
  
          </div>
  


  <span class="t-12 break-words block t-black--light t-normal
      global-nav__primary-link-text" title="Messaging">
    Messaging
  </span>
</a>

<!---->
<!----><!----><!---->          </li>
          <li class="global-nav__primary-item
              ">
                <a class="app-aware-link  global-nav__primary-link" target="_self" href="https://www.linkedin.com/notifications/?" data-test-app-aware-link="">
  
  <div id="ember244" class="global-nav__primary-link-notif artdeco-notification-badge ember-view">  <span class="notification-badge notification-badge--show ">
          <span aria-hidden="true" class="notification-badge__count ">1</span>
          <span class="a11y-text" data-test-notification-a11y="">1 new notification</span>
  </span>
  
    
    <div class="ivm-image-view-model    global-nav__icon-ivm
        ">
        
    <div class="ivm-view-attr__img-wrapper ivm-view-attr__img-wrapper--use-img-tag display-flex
        
        ">
        <li-icon aria-hidden="true" type="bell-fill" class=" " size="large"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-supported-dps="24x24" fill="currentColor" class="mercado-match" width="24" height="24" focusable="false">
  <path d="M22 19h-8.28a2 2 0 11-3.44 0H2v-1a4.52 4.52 0 011.17-2.83l1-1.17h15.7l1 1.17A4.42 4.42 0 0122 18zM18.21 7.44A6.27 6.27 0 0012 2a6.27 6.27 0 00-6.21 5.44L5 13h14z"></path>
</svg></li-icon>
    </div>
  
          </div>
  
  
</div>


  <span class="t-12 break-words block t-black--light t-normal
      global-nav__primary-link-text" title="Notifications">
    Notifications
  </span>
</a>

<!---->
<!----><!----><!---->          </li>
          <li class="global-nav__primary-item
              ">
<!---->              <div id="ember13" class="global-nav__me artdeco-dropdown artdeco-dropdown--placement-bottom artdeco-dropdown--justification-left ember-view">
  <button aria-expanded="false" id="ember14" class="global-nav__primary-link global-nav__primary-link-me-menu-trigger artdeco-dropdown__trigger artdeco-dropdown__trigger--placement-bottom ember-view" type="button" tabindex="0">
    <img width="24" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" height="24" alt="Harith Al-Safi" id="ember15" class="global-nav__me-photo evi-image ghost-person ember-view">

    <span class="global-nav__primary-link-text">
      Me
      <svg role="none" aria-hidden="true" class="global-nav__icon global-nav__icon--small" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" data-supported-dps="16x16" data-test-icon="caret-small">
<!---->    

    <use href="#caret-small" width="16" height="16"></use>
</svg>

    </span>
  
<!----></button>

  <div tabindex="-1" aria-hidden="true" id="ember16" class="global-nav__me-content artdeco-dropdown__content artdeco-dropdown--is-dropdown-element artdeco-dropdown__content--justification-right artdeco-dropdown__content--placement-bottom ember-view"><!----></div>
</div>

<!---->
<!----><!---->          </li>
          <li class="global-nav__primary-item
              ">
<!----><!---->              
  <button aria-expanded="false" class="global-nav__primary-link
      global-nav__primary-item--divider pl3
      global-nav__app-launcher-trigger" type="button">
  
      
    <div class="ivm-image-view-model    global-nav__icon-ivm">
        
    <div class="ivm-view-attr__img-wrapper ivm-view-attr__img-wrapper--use-img-tag display-flex
        
        ">
        <li-icon aria-hidden="true" type="grid" class=" " size="large"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-supported-dps="24x24" fill="currentColor" class="mercado-match" width="24" height="24" focusable="false">
  <path d="M3 3h4v4H3zm7 4h4V3h-4zm7-4v4h4V3zM3 14h4v-4H3zm7 0h4v-4h-4zm7 0h4v-4h-4zM3 21h4v-4H3zm7 0h4v-4h-4zm7 0h4v-4h-4z"></path>
</svg></li-icon>
    </div>
  
          </div>
  

    <span class="global-nav__primary-link-text" title="For Business">
      For Business
      <svg role="none" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" data-supported-dps="16x16" data-test-icon="caret-small">
<!---->    

    <use href="#caret-small" width="16" height="16"></use>
</svg>

    </span>
  
</button>

  <!---->


<div id="ember17" class="ember-view"><!----></div>
<!---->          </li>
          <li class="global-nav__primary-item
              ">
<!----><!----><!---->              <!---->
      
      <div class="premium-upsell-link">
        <a href="https://www.linkedin.com/premium/products/?family=JSS&amp;upsellOrderOrigin=premium_nav_upsell_text&amp;intentType=SEEK_JOB&amp;utype=job&amp;referenceId=%2FjM4QestQTuPyrwvSo4HnA%3D%3D&amp;destRedirectURL=https%3A%2F%2Fwww.linkedin.com%2Fin%2Fharith-al-safi%2Fdetails%2Feducation%2F" class="link-without-visited-state global-nav__primary-link global-nav__primary-link--premium global-nav__spotlight-upsell premium-upsell-link--extra-long">
          Get Hired Faster, Try Premium Free
        </a>
      </div>
  
  

          </li>

<!---->      </ul>
    </nav>
  </div>
</header>

    <div class="videoinappalert-inapp-alerts-manager
    hidden">
  
<!---->    
</div>

<!---->
<div class="authentication-outlet">
<!---->  <div id="profile-content" class="extended tetris pv-profile-body-wrapper">
  <div class="body">
    
  <div class="scaffold-layout__tracking-element"></div>

<div class="scaffold-layout
    scaffold-layout--breakpoint-xl
    scaffold-layout--main-aside
    
    scaffold-layout--reflow
    
     pv-profile
    pv-profile-detail--actions
    break-words">
    <section class="scaffold-layout-toolbar
    
    
    ">
  <div class="scaffold-layout-toolbar__content scaffold-layout-container
      scaffold-layout-container--reflow
      ">
    
      
      <div class="pv-profile-sticky-header-v2__container pv1">
  <div id="ember38" class="artdeco-entity-lockup artdeco-entity-lockup--size-1 ember-view pv-profile-sticky-header-v2__mini-profile-container">
    
<div class="presence-entity presence-entity--size-1 m1">
  <img src="https://media.licdn.com/dms/image/D4E03AQGB3OP3rlsmtQ/profile-displayphoto-shrink_100_100/0/1675373176223?e=1691625600&amp;v=beta&amp;t=-3k4RuOJvA8N9zuEKPE4wNyFxg7L6jKBLgCDUEe33ec" loading="lazy" alt="Harith Al-Safi" id="ember39" class="presence-entity__image   EntityPhoto-circle-1 evi-image lazy-image ember-view">

  
<div class="presence-entity__indicator
      
      presence-entity__indicator--size-1 presence-indicator
    presence-indicator--is-online
    presence-indicator--size-1">
  <span class="visually-hidden">
      Status is online
  </span>
</div>
</div>
    <div id="ember40" class="artdeco-entity-lockup__content ember-view overflow-hidden ml1 align-self-flex-start">
      <div id="ember41" class="artdeco-entity-lockup__title ember-view">
        Harith Al-Safi
<!---->      
</div>

      <div id="ember42" class="artdeco-entity-lockup__subtitle ember-view truncate">
        Software Engineer | Computer Engineer | AI Enthusiast 
      </div>
    </div>
  
</div>
  <div class="pv-profile-sticky-header-v2__actions-container">
    
<!---->      
  </div>
</div>
  
    
  </div>
</section>

  <div class="scaffold-layout__inner scaffold-layout-container
      scaffold-layout-container--reflow
      ">
<!---->
      <div class="scaffold-layout__row scaffold-layout__content
          scaffold-layout__content--main-aside
          
          
          scaffold-layout__content--has-aside
          
          ">
<!---->
          <main class="scaffold-layout__main">
  
            
        <section id="ember44" class="artdeco-card ember-view pb3"><!---->

            <div class="display-flex justify-flex-start align-items-center pt3 ph3">
    <button aria-label="Back to the main profile page" id="ember45" class="artdeco-button artdeco-button--circle artdeco-button--muted artdeco-button--3 artdeco-button--tertiary ember-view" type="button">  <li-icon aria-hidden="true" type="arrow-left" class="artdeco-button__icon"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" class="mercado-match" data-supported-dps="24x24" fill="currentColor" width="24" height="24" focusable="false">
  <path d="M9 4l-4.87 7H22v2H4.13L9 20H6.56L1 12l5.56-8z"></path>
</svg></li-icon>

<span class="artdeco-button__text">
    
</span></button>
    <div class="flex-grow-1 display-flex justify-space-between">
      <h2 class="t-20 t-bold ph3 pt3 pb2">
        Education
      </h2>
      <div class="display-flex align-items-center">
<!---->              <div class="">
        <div>
        <a class="optional-action-target-wrapper artdeco-button artdeco-button--tertiary artdeco-button--standard artdeco-button--3 artdeco-button--muted artdeco-button--circle
        inline-flex justify-center align-self-flex-start
        
        " target="_self" id="navigation-overlay-subsection-View-education-reorder-screen" href="https://www.linkedin.com/in/harith-al-safi/details/education/reorder?profileUrn=urn%3Ali%3Afsd_profile%3AACoAAC9P7scB1yv1hA-ZjtKBAxcuNQvmvu08uhI">
        <div class="pvs-navigation__icon">
          <li-icon type="sort" size="medium" role="img" aria-label="View education reorder screen"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-supported-dps="24x24" fill="currentColor" class="mercado-match" width="24" height="24" focusable="false">
  <path d="M20 7.56V10l-8-5.56L4 10V7.56L12 2zM4 14v2.44L12 22l8-5.56V14l-8 5.56z"></path>
</svg></li-icon>
        </div>
<!----><!---->    </a>

  </div>

    </div>

              <div class="">
        <div>
        <a class="optional-action-target-wrapper artdeco-button artdeco-button--tertiary artdeco-button--standard artdeco-button--3 artdeco-button--muted artdeco-button--circle
        inline-flex justify-center align-self-flex-start
        
        " target="_self" id="navigation-add-edit-deeplink-add-education" href="https://www.linkedin.com/in/harith-al-safi/add-edit/EDUCATION/?profileFormEntryPoint=PROFILE_SECTION&amp;trackingId=%2BS4WtlRzRCu5X%2BuHoH0KZg%3D%3D&amp;desktopBackground=PROFILE_DETAIL_SCREEN">
        <div class="pvs-navigation__icon">
          <li-icon type="add" size="medium" role="img" aria-label="Add new education"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-supported-dps="24x24" fill="currentColor" class="mercado-match" width="24" height="24" focusable="false">
  <path d="M21 13h-8v8h-2v-8H3v-2h8V3h2v8h8z"></path>
</svg></li-icon>
        </div>
<!----><!---->    </a>

  </div>

    </div>

      </div>
    </div>
  </div>

                  <div class="pvs-list__container">
    <div class="scaffold-finite-scroll
    scaffold-finite-scroll--infinite
    ">
  <!---->
  
      <div class="scaffold-finite-scroll__content">
        
          <ul class="pvs-list " tabindex="-1">
              <li class="pvs-list__paged-list-item artdeco-list__item pvs-list__item--line-separated pvs-list__item--one-column" id="profilePagedListComponent-ACoAAC9P7scB1yv1hA-ZjtKBAxcuNQvmvu08uhI-EDUCATION-VIEW-DETAILS-profile-ACoAAC9P7scB1yv1hA-ZjtKBAxcuNQvmvu08uhI-NONE-en-US-0">
                <div>
  
                        <!----><div class="pvs-entity
    pvs-entity--padded pvs-list__item--no-padding-in-columns
    
    ">
  <div>
        <a class="optional-action-target-wrapper 
        display-flex" target="_self" href="https://www.linkedin.com/company/7244/">
<!---->        
    <div class="ivm-image-view-model  pvs-entity__image ">
        
    <div class="ivm-view-attr__img-wrapper ivm-view-attr__img-wrapper--use-img-tag display-flex
        
        ">
<!---->          <img width="48" src="https://media.licdn.com/dms/image/C4E0BAQE0CKeyyA6TaQ/company-logo_100_100/0/1519856237427?e=1694044800&amp;v=beta&amp;t=OHsw5XosIzh7x6AsCuDXa1yufRcUCCM9f0Vi00UFv2s" loading="lazy" height="48" alt="University of Leeds logo" id="ember46" class="ivm-view-attr__img--centered EntityPhoto-square-3   evi-image lazy-image ember-view">
    </div>
  
          </div>
  
    </a>

  </div>

  <div class="display-flex flex-column full-width align-self-center">
    <div class="display-flex flex-row justify-space-between">
          <a class="optional-action-target-wrapper 
          display-flex flex-column full-width" target="_self" href="https://www.linkedin.com/company/7244/">
        <div class="display-flex flex-wrap align-items-center full-height">
              <div class="display-flex ">
    <div class="
      display-flex full-width">
    
      <div class="display-flex align-items-center
          mr1 hoverable-link-text t-bold">
        <span aria-hidden="true"><!---->University of Leeds<!----></span><span class="visually-hidden"><!---->University of Leeds<!----></span>
      </div>
  
  </div>

</div>
<!----><!----><!---->        </div>
            <span class="t-14 t-normal">
              <span aria-hidden="true"><!---->Bachelor of Engineering - BEng, Electronics and Computer Engineering<!----></span><span class="visually-hidden"><!---->Bachelor of Engineering - BEng, Electronics and Computer Engineering<!----></span>
            </span>
          <span class="t-14 t-normal t-black--light">
            <span aria-hidden="true"><!---->Sep 2020 - Jul 2024<!----></span><span class="visually-hidden"><!---->Sep 2020 - Jul 2024<!----></span>
          </span>
<!---->      </a>


<!---->
      <div class="pvs-entity__action-container">
              <div class="">
        <div>
        <a class="optional-action-target-wrapper artdeco-button artdeco-button--tertiary artdeco-button--standard artdeco-button--3 artdeco-button--muted artdeco-button--circle
        inline-flex justify-center align-self-flex-start
        
        " target="_self" id="navigation-add-edit-deeplink-edit-education" href="https://www.linkedin.com/in/harith-al-safi/add-edit/EDUCATION/?profileFormEntryPoint=PROFILE_SECTION&amp;entityUrn=urn%3Ali%3Afsd_profileEducation%3A%28ACoAAC9P7scB1yv1hA-ZjtKBAxcuNQvmvu08uhI%2C638675277%29&amp;trackingId=kXXYA3h%2FQv6feRRNCmgEAA%3D%3D&amp;desktopBackground=PROFILE_DETAIL_SCREEN">
        <div class="pvs-navigation__icon">
          <li-icon type="edit" size="medium" role="img" aria-label="Edit education University of Leeds"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-supported-dps="24x24" fill="currentColor" class="mercado-match" width="24" height="24" focusable="false">
  <path d="M21.13 2.86a3 3 0 00-4.17 0l-13 13L2 22l6.19-2L21.13 7a3 3 0 000-4.16zM6.77 18.57l-1.35-1.34L16.64 6 18 7.35z"></path>
</svg></li-icon>
        </div>
<!----><!---->    </a>

  </div>

    </div>

      </div>
    </div>

      <div class="pvs-list__outer-container">
<!---->    <ul class="pvs-list
        
        
        ">
        <li class=" pvs-list__item--one-column">
                <div class="pvs-list__outer-container">
<!---->    <ul class="pvs-list
        
        
        ">
        <li class="pvs-list__item--with-top-padding pvs-list__item--one-column">
                <div class="display-flex ">
    <div class="
      display-flex full-width">
    
      <div class="display-flex align-items-center
          t-14 t-normal t-black">
        <span aria-hidden="true"><!---->A hybrid course between Electronics Engineering and Computer Science<!----></span><span class="visually-hidden"><!---->A hybrid course between Electronics Engineering and Computer Science<!----></span>
      </div>
  
  </div>

</div>

        </li>
    </ul>
<!----></div>

        </li>
        <li class=" pvs-list__item--one-column">
                <div class="pvs-list__outer-container">
<!---->    <ul class="pvs-list
        
        
        ">
        <li class="pvs-list__item--with-top-padding pvs-list__item--one-column">
                <div class="display-flex ">
    <div class="
      display-flex full-width">
    
      <div class="display-flex align-items-center
          t-14 t-normal t-black">
        <span aria-hidden="true"><strong><!---->Skills:<!----></strong><span class="white-space-pre"> </span>Assembly Language · Git · Digital Electronics · Algorithms and Data structure · Mathematics · Computer Science · Field-Programmable Gate Arrays (FPGA) · C++ · Mbed · Digital Signal Processing · Embedded Systems · Bash · Qt Creator · Hardware Description Language · Circuit Design · Team Leadership · Communication · LaTeX · Computer Networking · Java · MATLAB · Linux<!----></span><span class="visually-hidden"><strong><!---->Skills:<!----></strong><span class="white-space-pre"> </span>Assembly Language · Git · Digital Electronics · Algorithms and Data structure · Mathematics · Computer Science · Field-Programmable Gate Arrays (FPGA) · C++ · Mbed · Digital Signal Processing · Embedded Systems · Bash · Qt Creator · Hardware Description Language · Circuit Design · Team Leadership · Communication · LaTeX · Computer Networking · Java · MATLAB · Linux<!----></span>
      </div>
  
  </div>

</div>

        </li>
    </ul>
<!----></div>

        </li>
        <li class=" pvs-list__item--one-column">
                <div class="pvs-list__outer-container">
<!----><!----><!----></div>

        </li>
    </ul>
<!----></div>
  </div>
</div>

                
</div>

              </li>
              <li class="pvs-list__paged-list-item artdeco-list__item pvs-list__item--line-separated pvs-list__item--one-column" id="profilePagedListComponent-ACoAAC9P7scB1yv1hA-ZjtKBAxcuNQvmvu08uhI-EDUCATION-VIEW-DETAILS-profile-ACoAAC9P7scB1yv1hA-ZjtKBAxcuNQvmvu08uhI-NONE-en-US-1">
                <div>
  
                        <!----><div class="pvs-entity
    pvs-entity--padded pvs-list__item--no-padding-in-columns
    
    ">
  <div>
        <a class="optional-action-target-wrapper 
        display-flex" target="_self" href="https://www.linkedin.com/company/7244/">
<!---->        
    <div class="ivm-image-view-model  pvs-entity__image ">
        
    <div class="ivm-view-attr__img-wrapper ivm-view-attr__img-wrapper--use-img-tag display-flex
        
        ">
<!---->          <img width="48" src="https://media.licdn.com/dms/image/C4E0BAQE0CKeyyA6TaQ/company-logo_100_100/0/1519856237427?e=1694044800&amp;v=beta&amp;t=OHsw5XosIzh7x6AsCuDXa1yufRcUCCM9f0Vi00UFv2s" loading="lazy" height="48" alt="University of Leeds logo" id="ember47" class="ivm-view-attr__img--centered EntityPhoto-square-3   evi-image lazy-image ember-view">
    </div>
  
          </div>
  
    </a>

  </div>

  <div class="display-flex flex-column full-width align-self-center">
    <div class="display-flex flex-row justify-space-between">
          <a class="optional-action-target-wrapper 
          display-flex flex-column full-width" target="_self" href="https://www.linkedin.com/company/7244/">
        <div class="display-flex flex-wrap align-items-center full-height">
              <div class="display-flex ">
    <div class="
      display-flex full-width">
    
      <div class="display-flex align-items-center
          mr1 hoverable-link-text t-bold">
        <span aria-hidden="true"><!---->University of Leeds<!----></span><span class="visually-hidden"><!---->University of Leeds<!----></span>
      </div>
  
  </div>

</div>
<!----><!----><!---->        </div>
            <span class="t-14 t-normal">
              <span aria-hidden="true"><!---->Foundation degree, Engineering<!----></span><span class="visually-hidden"><!---->Foundation degree, Engineering<!----></span>
            </span>
          <span class="t-14 t-normal t-black--light">
            <span aria-hidden="true"><!---->2019 - 2020<!----></span><span class="visually-hidden"><!---->2019 - 2020<!----></span>
          </span>
<!---->      </a>


<!---->
      <div class="pvs-entity__action-container">
              <div class="">
        <div>
        <a class="optional-action-target-wrapper artdeco-button artdeco-button--tertiary artdeco-button--standard artdeco-button--3 artdeco-button--muted artdeco-button--circle
        inline-flex justify-center align-self-flex-start
        
        " target="_self" id="navigation-add-edit-deeplink-edit-education" href="https://www.linkedin.com/in/harith-al-safi/add-edit/EDUCATION/?profileFormEntryPoint=PROFILE_SECTION&amp;entityUrn=urn%3Ali%3Afsd_profileEducation%3A%28ACoAAC9P7scB1yv1hA-ZjtKBAxcuNQvmvu08uhI%2C695360173%29&amp;trackingId=pOjzk5T8TfmaNRELr5OD2Q%3D%3D&amp;desktopBackground=PROFILE_DETAIL_SCREEN">
        <div class="pvs-navigation__icon">
          <li-icon type="edit" size="medium" role="img" aria-label="Edit education University of Leeds"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-supported-dps="24x24" fill="currentColor" class="mercado-match" width="24" height="24" focusable="false">
  <path d="M21.13 2.86a3 3 0 00-4.17 0l-13 13L2 22l6.19-2L21.13 7a3 3 0 000-4.16zM6.77 18.57l-1.35-1.34L16.64 6 18 7.35z"></path>
</svg></li-icon>
        </div>
<!----><!---->    </a>

  </div>

    </div>

      </div>
    </div>

      <div class="pvs-list__outer-container">
<!---->    <ul class="pvs-list
        
        
        ">
        <li class=" pvs-list__item--one-column">
                <div class="
    display-flex mv1 align-items-center">
    <div class="display-flex link-without-hover-visited">
    
<!---->      <div class="display-flex ">
    <div class="
      display-flex full-width">
    
      
  <div class="pv-shared-text-with-see-more full-width t-14 t-normal t-black display-flex align-items-center">
    <div class="inline-show-more-text
    inline-show-more-text--is-collapsed
    inline-show-more-text--is-collapsed-with-line-clamp
    
    
     full-width" style="-webkit-line-clamp:4;" tabindex="-1">

    <span aria-hidden="true"><!---->Grade: 93/100<!----></span><span class="visually-hidden"><!---->Grade: 93/100<!----></span>

<!----></div>
  </div>

  
  </div>

</div>
  
  </div>

<!----></div>

        </li>
        <li class=" pvs-list__item--one-column">
                <div class="pvs-list__outer-container">
<!---->    <ul class="pvs-list
        
        
        ">
        <li class="pvs-list__item--with-top-padding pvs-list__item--one-column">
                <div class="display-flex ">
    <div class="
      display-flex full-width">
    
      <div class="display-flex align-items-center
          t-14 t-normal t-black">
        <span aria-hidden="true"><!---->We took higher level pure and applied mathematics in addition to CAD designs with automobiles. I also took external courses on python, octave and multivariable calculus.<!----></span><span class="visually-hidden"><!---->We took higher level pure and applied mathematics in addition to CAD designs with automobiles. I also took external courses on python, octave and multivariable calculus.<!----></span>
      </div>
  
  </div>

</div>

        </li>
    </ul>
<!----></div>

        </li>
        <li class=" pvs-list__item--one-column">
                <div class="pvs-list__outer-container">
<!---->    <ul class="pvs-list
        
        
        ">
        <li class="pvs-list__item--with-top-padding pvs-list__item--one-column">
                <div class="display-flex ">
    <div class="
      display-flex full-width">
    
      <div class="display-flex align-items-center
          t-14 t-normal t-black">
        <span aria-hidden="true"><strong><!---->Skills:<!----></strong><span class="white-space-pre"> </span>Mathematics · Microsoft Office · AutoCAD<!----></span><span class="visually-hidden"><strong><!---->Skills:<!----></strong><span class="white-space-pre"> </span>Mathematics · Microsoft Office · AutoCAD<!----></span>
      </div>
  
  </div>

</div>

        </li>
    </ul>
<!----></div>

        </li>
        <li class=" pvs-list__item--one-column">
                <div class="pvs-list__outer-container">
<!----><!----><!----></div>

        </li>
    </ul>
<!----></div>
  </div>
</div>

                
</div>

              </li>
              <li class="pvs-list__paged-list-item artdeco-list__item pvs-list__item--line-separated pvs-list__item--one-column" id="profilePagedListComponent-ACoAAC9P7scB1yv1hA-ZjtKBAxcuNQvmvu08uhI-EDUCATION-VIEW-DETAILS-profile-ACoAAC9P7scB1yv1hA-ZjtKBAxcuNQvmvu08uhI-NONE-en-US-2">
                <div>
  
                        <!----><div class="pvs-entity
    pvs-entity--padded pvs-list__item--no-padding-in-columns
    
    ">
  <div>
      <div class="
        display-flex" tabindex="-1" aria-hidden="true">
    
<!---->        
    <div class="ivm-image-view-model  pvs-entity__image ">
        
    <div class="ivm-view-attr__img-wrapper ivm-view-attr__img-wrapper--use-img-tag display-flex
        
        ">
        <div class="EntityPhoto-square-3-ghost-school ivm-view-attr__ghost-entity  ">
<!---->        </div>
    </div>
  
          </div>
  
    
  </div>

  </div>

  <div class="display-flex flex-column full-width align-self-center">
    <div class="display-flex flex-row justify-space-between">
          <a class="optional-action-target-wrapper 
          display-flex flex-column full-width" target="_self" href="https://www.linkedin.com/search/results/all/?keywords=Cambridge+high+school++">
        <div class="display-flex flex-wrap align-items-center full-height">
              <div class="display-flex ">
    <div class="
      display-flex full-width">
    
      <div class="display-flex align-items-center
          mr1 hoverable-link-text t-bold">
        <span aria-hidden="true"><!---->Cambridge high school<span class="white-space-pre"> </span></span><span class="visually-hidden"><!---->Cambridge high school<span class="white-space-pre"> </span></span>
      </div>
  
  </div>

</div>
<!----><!----><!---->        </div>
            <span class="t-14 t-normal">
              <span aria-hidden="true"><!---->High School Diploma, IB<span class="white-space-pre"> </span></span><span class="visually-hidden"><!---->High School Diploma, IB<span class="white-space-pre"> </span></span>
            </span>
          <span class="t-14 t-normal t-black--light">
            <span aria-hidden="true"><!---->2017 - 2019<!----></span><span class="visually-hidden"><!---->2017 - 2019<!----></span>
          </span>
<!---->      </a>


<!---->
      <div class="pvs-entity__action-container">
              <div class="">
        <div>
        <a class="optional-action-target-wrapper artdeco-button artdeco-button--tertiary artdeco-button--standard artdeco-button--3 artdeco-button--muted artdeco-button--circle
        inline-flex justify-center align-self-flex-start
        
        " target="_self" id="navigation-add-edit-deeplink-edit-education" href="https://www.linkedin.com/in/harith-al-safi/add-edit/EDUCATION/?profileFormEntryPoint=PROFILE_SECTION&amp;entityUrn=urn%3Ali%3Afsd_profileEducation%3A%28ACoAAC9P7scB1yv1hA-ZjtKBAxcuNQvmvu08uhI%2C695359238%29&amp;trackingId=KnuUvtWcRsqUzViyeIcKTA%3D%3D&amp;desktopBackground=PROFILE_DETAIL_SCREEN">
        <div class="pvs-navigation__icon">
          <li-icon type="edit" size="medium" role="img" aria-label="Edit education Cambridge high school  "><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-supported-dps="24x24" fill="currentColor" class="mercado-match" width="24" height="24" focusable="false">
  <path d="M21.13 2.86a3 3 0 00-4.17 0l-13 13L2 22l6.19-2L21.13 7a3 3 0 000-4.16zM6.77 18.57l-1.35-1.34L16.64 6 18 7.35z"></path>
</svg></li-icon>
        </div>
<!----><!---->    </a>

  </div>

    </div>

      </div>
    </div>

      <div class="pvs-list__outer-container">
<!---->    <ul class="pvs-list
        
        
        ">
        <li class=" pvs-list__item--one-column">
                <div class="
    display-flex mv1 align-items-center">
    <div class="display-flex link-without-hover-visited">
    
<!---->      <div class="display-flex ">
    <div class="
      display-flex full-width">
    
      
  <div class="pv-shared-text-with-see-more full-width t-14 t-normal t-black display-flex align-items-center">
    <div class="inline-show-more-text
    inline-show-more-text--is-collapsed
    inline-show-more-text--is-collapsed-with-line-clamp
    
    
     full-width" style="-webkit-line-clamp:4;" tabindex="-1">

    <span aria-hidden="true"><!---->Grade: 40/42<!----></span><span class="visually-hidden"><!---->Grade: 40/42<!----></span>

<!----></div>
  </div>

  
  </div>

</div>
  
  </div>

<!----></div>

        </li>
        <li class=" pvs-list__item--one-column">
                <div class="
    display-flex mv1 align-items-center">
    <div class="display-flex link-without-hover-visited">
    
<!---->      <div class="display-flex ">
    <div class="
      display-flex full-width">
    
      
  <div class="pv-shared-text-with-see-more full-width t-14 t-normal t-black display-flex align-items-center">
    <div class="inline-show-more-text
    inline-show-more-text--is-collapsed
    inline-show-more-text--is-collapsed-with-line-clamp
    
    
     full-width" style="-webkit-line-clamp:4;" tabindex="-1">

    <span aria-hidden="true"><!---->Activities and societies: CAS activities in addition to extra math courses<!----></span><span class="visually-hidden"><!---->Activities and societies: CAS activities in addition to extra math courses<!----></span>

<!----></div>
  </div>

  
  </div>

</div>
  
  </div>

<!----></div>

        </li>
        <li class=" pvs-list__item--one-column">
                <div class="pvs-list__outer-container">
<!---->    <ul class="pvs-list
        
        
        ">
        <li class="pvs-list__item--with-top-padding pvs-list__item--one-column">
                <div class="display-flex ">
    <div class="
      display-flex full-width">
    
      <div class="display-flex align-items-center
          t-14 t-normal t-black">
        <span aria-hidden="true"><!---->My subjects were:<!----><br><!---->Math Standard Level<!----><br><!---->English B Standard Level<!----><br><!---->Arabic B Standard Level<!----><br><!---->Physics Higher Level<!----><br><!---->Chemistry Higher Level<!----><br><!---->Economics Standard Level<!----></span><span class="visually-hidden"><!---->My subjects were:
Math Standard Level
English B Standard Level
Arabic B Standard Level
Physics Higher Level
Chemistry Higher Level
Economics Standard Level<!----></span>
      </div>
  
  </div>

</div>

        </li>
    </ul>
<!----></div>

        </li>
        <li class=" pvs-list__item--one-column">
                <div class="pvs-list__outer-container">
<!---->    <ul class="pvs-list
        
        
        ">
        <li class="pvs-list__item--with-top-padding pvs-list__item--one-column">
                <div class="display-flex ">
    <div class="
      display-flex full-width">
    
      <div class="display-flex align-items-center
          t-14 t-normal t-black">
        <span aria-hidden="true"><strong><!---->Skills:<!----></strong><span class="white-space-pre"> </span>Mathematics · Microsoft Office<!----></span><span class="visually-hidden"><strong><!---->Skills:<!----></strong><span class="white-space-pre"> </span>Mathematics · Microsoft Office<!----></span>
      </div>
  
  </div>

</div>

        </li>
    </ul>
<!----></div>

        </li>
        <li class=" pvs-list__item--one-column">
                <div class="pvs-list__outer-container">
<!----><!----><!----></div>

        </li>
    </ul>
<!----></div>
  </div>
</div>

                
</div>

              </li>
          </ul>
      
      </div>
    

<!---->
    <div>
  
<!---->    
</div>

</div>
</div>

        </section>
  
          
</main>

          <aside class="scaffold-layout__aside
    
    ">
  
            
      <!---->
  <!---->

<!---->
      <section id="ember71" class="artdeco-card ember-view mb2"><!---->

  <section class="pt5 ph5">
    <h2 class="text-heading-medium">People also viewed</h2>

<!---->
    <ul class="mt4">
          <li class="pv-browsemap-section__member-container ">

    <a href="/in/daniel-mohammed-57a450223/" id="ember72" class="ember-view display-flex link-without-hover-visited">
      <img width="48" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" loading="lazy" height="48" id="ember73" class="evi-image lazy-image EntityPhoto-circle-3 flex-shrink-zero mr3 ghost-person ember-view">
<div class="pv-browsemap-section__member-detail">
  <h3 class="actor-name-with-distance t-16 t-black t-bold
     pv-browsemap-section__member-detail--has-hover">
    <span class="name-and-icon"><span class="name">Daniel Mohammed</span>
        <span class="distance-and-badge">
          <span class="distance-badge t-black--light t-14
    separator
    t-black--light
    
    ">
  <span class="visually-hidden">
      1st degree connection
  </span>
  <span class="dist-value " aria-hidden="true">
    1st
  </span>
</span><!---->        </span>
</span>

  
</h3>
  <p class="pv-browsemap-section-v2__member-headline">
    <div class="inline-show-more-text
    inline-show-more-text--is-collapsed
    inline-show-more-text--is-collapsed-with-line-clamp
    
    
    " style="-webkit-line-clamp:2;" tabindex="-1">

    Software Engineer (Student &amp; Intern)
  
<!----></div>
  </p>
</div>
    </a>
    <div class="ml7 mt1 pl3 pb2">
    <!---->
<!---->
<!---->
        

    <div class="entry-point">
      
    <div></div>
  

          
      <button aria-label="Message Daniel" id="ember74" class="artdeco-button artdeco-button--muted artdeco-button--2 artdeco-button--secondary ember-view">  <li-icon aria-hidden="true" type="send-privately" class="artdeco-button__icon" size="small"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" data-supported-dps="16x16" fill="currentColor" class="mercado-match" width="16" height="16" focusable="false">
  <path d="M14 2L0 6.67l5 2.64 5.67-3.98L6.7 11l2.63 5L14 2z"></path>
</svg></li-icon>

<span class="artdeco-button__text">
    Message
</span></button>
    
    </div>
  


<!---->
<!---->
<!---->
<!---->
<!---->
<!---->
<!---->


  </div>


</li>
          <li class="pv-browsemap-section__member-container ">

    <a href="/in/kumar-acharjee-a14335202/" id="ember75" class="ember-view display-flex link-without-hover-visited">
      <img width="48" src="https://media.licdn.com/dms/image/D4E03AQF1efEgqH1BHg/profile-displayphoto-shrink_100_100/0/1665533472534?e=1691625600&amp;v=beta&amp;t=OhaHoh3-1NnTF1k-H_Yz9-1un-wKK_WjGkSQGR38YXs" loading="lazy" height="48" id="ember76" class="evi-image lazy-image EntityPhoto-circle-3 flex-shrink-zero mr3 ember-view">
<div class="pv-browsemap-section__member-detail">
  <h3 class="actor-name-with-distance t-16 t-black t-bold
     pv-browsemap-section__member-detail--has-hover">
    <span class="name-and-icon"><span class="name">Kumar Acharjee</span>
        <span class="distance-and-badge">
          <span class="distance-badge t-black--light t-14
    separator
    t-black--light
    
    ">
  <span class="visually-hidden">
      1st degree connection
  </span>
  <span class="dist-value " aria-hidden="true">
    1st
  </span>
</span><!---->        </span>
</span>

  
</h3>
  <p class="pv-browsemap-section-v2__member-headline">
    <div class="inline-show-more-text
    inline-show-more-text--is-collapsed
    inline-show-more-text--is-collapsed-with-line-clamp
    
    
    " style="-webkit-line-clamp:2;" tabindex="-1">

    Software Engineer Intern at Johnson Controls
  
<!----></div>
  </p>
</div>
    </a>
    <div class="ml7 mt1 pl3 pb2">
    <!---->
<!---->
<!---->
        

    <div class="entry-point">
      
    <div></div>
  

          
      <button aria-label="Message Kumar" id="ember77" class="artdeco-button artdeco-button--muted artdeco-button--2 artdeco-button--secondary ember-view">  <li-icon aria-hidden="true" type="send-privately" class="artdeco-button__icon" size="small"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" data-supported-dps="16x16" fill="currentColor" class="mercado-match" width="16" height="16" focusable="false">
  <path d="M14 2L0 6.67l5 2.64 5.67-3.98L6.7 11l2.63 5L14 2z"></path>
</svg></li-icon>

<span class="artdeco-button__text">
    Message
</span></button>
    
    </div>
  


<!---->
<!---->
<!---->
<!---->
<!---->
<!---->
<!---->


  </div>


</li>
          <li class="pv-browsemap-section__member-container ">

    <a href="/in/laith-alfar-096467209/" id="ember78" class="ember-view display-flex link-without-hover-visited">
      <img width="48" src="https://media.licdn.com/dms/image/C4E03AQHXMDwW3ihZ0Q/profile-displayphoto-shrink_100_100/0/1615556592638?e=1691625600&amp;v=beta&amp;t=8UTcZcvsLEcXP2TL9KZuf83FaFfAJMBSGF2eQrpON-s" loading="lazy" height="48" id="ember79" class="evi-image lazy-image EntityPhoto-circle-3 flex-shrink-zero mr3 ember-view">
<div class="pv-browsemap-section__member-detail">
  <h3 class="actor-name-with-distance t-16 t-black t-bold
     pv-browsemap-section__member-detail--has-hover">
    <span class="name-and-icon"><span class="name">Laith Alfar</span>
        <span class="distance-and-badge">
          <span class="distance-badge t-black--light t-14
    separator
    t-black--light
    
    ">
  <span class="visually-hidden">
      1st degree connection
  </span>
  <span class="dist-value " aria-hidden="true">
    1st
  </span>
</span><!---->        </span>
</span>

  
</h3>
  <p class="pv-browsemap-section-v2__member-headline">
    <div class="inline-show-more-text
    inline-show-more-text--is-collapsed
    inline-show-more-text--is-collapsed-with-line-clamp
    
    
    " style="-webkit-line-clamp:2;" tabindex="-1">

    3rd year Electronics and Computer engineer at University of Nottingham
  
<!---->
<!----></div>
  </p>
</div>
    </a>
    <div class="ml7 mt1 pl3 pb2">
    <!---->
<!---->
<!---->
        

    <div class="entry-point">
      
    <div></div>
  

          
      <button aria-label="Message Laith" id="ember80" class="artdeco-button artdeco-button--muted artdeco-button--2 artdeco-button--secondary ember-view">  <li-icon aria-hidden="true" type="send-privately" class="artdeco-button__icon" size="small"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" data-supported-dps="16x16" fill="currentColor" class="mercado-match" width="16" height="16" focusable="false">
  <path d="M14 2L0 6.67l5 2.64 5.67-3.98L6.7 11l2.63 5L14 2z"></path>
</svg></li-icon>

<span class="artdeco-button__text">
    Message
</span></button>
    
    </div>
  


<!---->
<!---->
<!---->
<!---->
<!---->
<!---->
<!---->


  </div>


</li>
          <li class="pv-browsemap-section__member-container ">

    <a href="/in/randa-thabit/" id="ember81" class="ember-view display-flex link-without-hover-visited">
      <img width="48" src="https://media.licdn.com/dms/image/C4D03AQEFpGSRVWm5Dw/profile-displayphoto-shrink_100_100/0/1643728095379?e=1691625600&amp;v=beta&amp;t=NsE63iy6sIGDi8qYksh_aR5ysdu2cMTyX_2gUUw8bv8" loading="lazy" height="48" id="ember82" class="evi-image lazy-image EntityPhoto-circle-3 flex-shrink-zero mr3 ember-view">
<div class="pv-browsemap-section__member-detail">
  <h3 class="actor-name-with-distance t-16 t-black t-bold
     pv-browsemap-section__member-detail--has-hover">
    <span class="name-and-icon"><span class="name">Randa Thabit</span>
        <span class="distance-and-badge">
          <span class="distance-badge t-black--light t-14
    separator
    t-black--light
    
    ">
  <span class="visually-hidden">
      1st degree connection
  </span>
  <span class="dist-value " aria-hidden="true">
    1st
  </span>
</span><!---->        </span>
</span>

  
</h3>
  <p class="pv-browsemap-section-v2__member-headline">
    <div class="inline-show-more-text
    inline-show-more-text--is-collapsed
    inline-show-more-text--is-collapsed-with-line-clamp
    
    
    " style="-webkit-line-clamp:2;" tabindex="-1">

    PhD in electronic and electrical engineering
  
<!----></div>
  </p>
</div>
    </a>
    <div class="ml7 mt1 pl3 pb2">
    <!---->
<!---->
<!---->
        

    <div class="entry-point">
      
    <div></div>
  

          
      <button aria-label="Message Randa" id="ember83" class="artdeco-button artdeco-button--muted artdeco-button--2 artdeco-button--secondary ember-view">  <li-icon aria-hidden="true" type="send-privately" class="artdeco-button__icon" size="small"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" data-supported-dps="16x16" fill="currentColor" class="mercado-match" width="16" height="16" focusable="false">
  <path d="M14 2L0 6.67l5 2.64 5.67-3.98L6.7 11l2.63 5L14 2z"></path>
</svg></li-icon>

<span class="artdeco-button__text">
    Message
</span></button>
    
    </div>
  


<!---->
<!---->
<!---->
<!---->
<!---->
<!---->
<!---->


  </div>


</li>
          <li class="pv-browsemap-section__member-container ">

    <a href="/in/tiseolayinka/" id="ember84" class="ember-view display-flex link-without-hover-visited">
      <img width="48" src="https://media.licdn.com/dms/image/C4D03AQEtMjZoC8djXA/profile-displayphoto-shrink_100_100/0/1616591959890?e=1691625600&amp;v=beta&amp;t=MFQkQeiRGFiy-FJM_D4sonnD1d4JgwVgoaH62Wdzho8" loading="lazy" height="48" id="ember85" class="evi-image lazy-image EntityPhoto-circle-3 flex-shrink-zero mr3 ember-view">
<div class="pv-browsemap-section__member-detail">
  <h3 class="actor-name-with-distance t-16 t-black t-bold
     pv-browsemap-section__member-detail--has-hover">
    <span class="name-and-icon"><span class="name">Tise Olayinka</span>
        <span class="distance-and-badge">
          <span class="distance-badge t-black--light t-14
    separator
    t-black--light
    
    ">
  <span class="visually-hidden">
      1st degree connection
  </span>
  <span class="dist-value " aria-hidden="true">
    1st
  </span>
</span><!---->        </span>
</span>

  
</h3>
  <p class="pv-browsemap-section-v2__member-headline">
    <div class="inline-show-more-text
    inline-show-more-text--is-collapsed
    inline-show-more-text--is-collapsed-with-line-clamp
    
    
    " style="-webkit-line-clamp:2;" tabindex="-1">

    3rd Year Msc Mechatronics and Robotics Student at the University of Leeds
  
<!---->
<!----></div>
  </p>
</div>
    </a>
    <div class="ml7 mt1 pl3 pb2">
    <!---->
<!---->
<!---->
        

    <div class="entry-point">
      
    <div></div>
  

          
      <button aria-label="Message Tise" id="ember86" class="artdeco-button artdeco-button--muted artdeco-button--2 artdeco-button--secondary ember-view">  <li-icon aria-hidden="true" type="send-privately" class="artdeco-button__icon" size="small"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" data-supported-dps="16x16" fill="currentColor" class="mercado-match" width="16" height="16" focusable="false">
  <path d="M14 2L0 6.67l5 2.64 5.67-3.98L6.7 11l2.63 5L14 2z"></path>
</svg></li-icon>

<span class="artdeco-button__text">
    Message
</span></button>
    
    </div>
  


<!---->
<!---->
<!---->
<!---->
<!---->
<!---->
<!---->


  </div>


</li>
    </ul>

<!---->  </section>

    <footer class="artdeco-card__actions">
      <button aria-expanded="false" id="ember87" class="pv3 artdeco-button artdeco-button--muted artdeco-button--icon-right artdeco-button--2 artdeco-button--fluid artdeco-button--tertiary ember-view">  <li-icon aria-hidden="true" type="chevron-down" class="artdeco-button__icon" size="small"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" data-supported-dps="16x16" fill="currentColor" class="mercado-match" width="16" height="16" focusable="false">
  <path d="M1 5l7 4.61L15 5v2.39L8 12 1 7.39z"></path>
</svg></li-icon>

<span class="artdeco-button__text">
    Show more
</span></button>
    </footer>
</section>

<!---->
<!---->
<!---->
  
          
</aside>
      </div>

<!---->  </div>
</div>
<!---->
<footer class="global-footer
    global-footer--static">
  
        <div id="ember24" class="ember-view   ">
            
    <div id="expanded-footer" class="global-footer__container">
<!---->
      <div class="grid grid--is-nested grid--no-gutters mv3">
        <nav class="grid__col
            grid__col--12">
          <ul class="grid grid--no-gutters grid--is-nested">
              <li class="global-footer__link-container grid__col
                  grid__col--8">
                  <a tabindex="0" target="_blank" href="https://about.linkedin.com/" id="globalfooter-about" class="ember-view global-footer__link global-footer__link--static t-12 t-bold">
                    About
                  </a>
              </li>
              <li class="global-footer__link-container grid__col
                  grid__col--8">
                  <a tabindex="0" target="_blank" href="https://www.linkedin.com/accessibility" id="globalfooter-accessibility" class="ember-view global-footer__link global-footer__link--static t-12 t-bold">
                    Accessibility
                  </a>
              </li>
              <li class="global-footer__link-container grid__col
                  grid__col--8">
                  <a tabindex="0" target="_blank" href="https://business.linkedin.com/talent-solutions?trk=flagship_nav&amp;veh=li-footer-lts-control&amp;src=li-footer" id="globalfooter-talent_solutions" class="ember-view global-footer__link global-footer__link--static t-12 t-bold">
                    Talent Solutions
                  </a>
              </li>
              <li class="global-footer__link-container grid__col
                  grid__col--8">
                  <a tabindex="0" target="_blank" href="https://www.linkedin.com/legal/professional-community-policies" id="globalfooter-community_guidelines" class="ember-view global-footer__link global-footer__link--static t-12 t-bold">
                    Community Guidelines
                  </a>
              </li>
              <li class="global-footer__link-container grid__col
                  grid__col--8">
                  <a tabindex="0" target="_blank" href="https://careers.linkedin.com/" id="globalfooter-careers" class="ember-view global-footer__link global-footer__link--static t-12 t-bold">
                    Careers
                  </a>
              </li>
              <li class="global-footer__link-container grid__col
                  grid__col--8">
                  <a tabindex="0" target="_blank" href="https://business.linkedin.com/marketing-solutions?trk=n_nav_lms_f&amp;src=li-footer" id="globalfooter-marketing_solutions" class="ember-view global-footer__link global-footer__link--static t-12 t-bold">
                    Marketing Solutions
                  </a>
              </li>
              <li class="global-footer__link-container grid__col
                  grid__col--8">
                  
<div id="ember57" class="artdeco-dropdown artdeco-dropdown--placement-top artdeco-dropdown--justification-left ember-view global-footer-dropdown">
  <button aria-expanded="false" id="globalfooter-privacy_dropdown-trigger" class="artdeco-dropdown__trigger artdeco-dropdown__trigger--placement-top ember-view global-footer-dropdown__trigger" type="button" tabindex="0">
    <span class="global-footer__link global-footer__link--static t-12 t-bold">
      <span class="text-align-left">
        Privacy &amp; Terms
        <svg role="none" aria-hidden="true" class="global-footer-dropdown__trigger-icon" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" data-supported-dps="16x16" data-test-icon="caret-small">
<!---->    

    <use href="#caret-small" width="16" height="16"></use>
</svg>

      </span>
    </span>
  
<!----></button>
  <div tabindex="-1" aria-hidden="true" id="ember59" class="artdeco-dropdown__content artdeco-dropdown--is-dropdown-element artdeco-dropdown__content--justification-left artdeco-dropdown__content--placement-top ember-view global-footer-dropdown__options"><div class="artdeco-dropdown__content-inner">
  
    
  <ul>
      <li class="global-footer-dropdown__item" id="privacy-policy-footer-link">
          <a tabindex="0" target="_blank" href="https://www.linkedin.com/static?key=privacy_policy" id="ember60" class="ember-view global-footer-dropdown__link block pv1 ph4 t-black t-12">
            Privacy Policy
          </a>
      </li>
      <li class="global-footer-dropdown__item" id="user-agreement-footer-link">
          <a tabindex="0" target="_blank" href="https://www.linkedin.com/static?key=user_agreement" id="ember61" class="ember-view global-footer-dropdown__link block pv1 ph4 t-black t-12">
            User Agreement
          </a>
      </li>
      <li class="global-footer-dropdown__item" id="pages_terms-footer-link">
          <a tabindex="0" target="_blank" href="https://www.linkedin.com/legal/l/linkedin-pages-terms" id="ember62" class="ember-view global-footer-dropdown__link block pv1 ph4 t-black t-12">
            Pages terms
          </a>
      </li>
      <li class="global-footer-dropdown__item" id="cookie-policy-footer-link">
          <a tabindex="0" target="_blank" href="https://www.linkedin.com/legal/cookie-policy" id="ember63" class="ember-view global-footer-dropdown__link block pv1 ph4 t-black t-12">
            Cookie Policy
          </a>
      </li>
      <li class="global-footer-dropdown__item" id="copyright-policy-footer-link">
          <a tabindex="0" target="_blank" href="https://www.linkedin.com/static?key=copyright_policy" id="ember64" class="ember-view global-footer-dropdown__link block pv1 ph4 t-black t-12">
            Copyright Policy
          </a>
      </li>
  </ul>

  
</div>
</div>
</div>
              </li>
              <li class="global-footer__link-container grid__col
                  grid__col--8">
                  <a tabindex="0" target="_blank" href="https://www.linkedin.com/help/linkedin/answer/62931" id="globalfooter-ad_choices" class="ember-view global-footer__link global-footer__link--static t-12 t-bold">
                    Ad Choices
                  </a>
              </li>
              <li class="global-footer__link-container grid__col
                  grid__col--8">
                  <a tabindex="0" target="_blank" href="https://business.linkedin.com/marketing-solutions/ads?trk=n_nav_ads_f" id="globalfooter-advertising" class="ember-view global-footer__link global-footer__link--static t-12 t-bold">
                    Advertising
                  </a>
              </li>
              <li class="global-footer__link-container grid__col
                  grid__col--8">
                  <a tabindex="0" target="_blank" href="https://business.linkedin.com/sales-solutions?trk=flagship_nav&amp;veh=li-footer-lss-control&amp;src=li-footer" id="globalfooter-sales_solutions" class="ember-view global-footer__link global-footer__link--static t-12 t-bold">
                    Sales Solutions
                  </a>
              </li>
              <li class="global-footer__link-container grid__col
                  grid__col--8">
                  <a tabindex="0" target="_blank" href="https://mobile.linkedin.com/" id="globalfooter-mobile" class="ember-view global-footer__link global-footer__link--static t-12 t-bold">
                    Mobile
                  </a>
              </li>
              <li class="global-footer__link-container grid__col
                  grid__col--8">
                  <a tabindex="0" target="_blank" href="https://smallbusiness.linkedin.com?&amp;src=li-footer" id="globalfooter-small_business" class="ember-view global-footer__link global-footer__link--static t-12 t-bold">
                    Small Business
                  </a>
              </li>
              <li class="global-footer__link-container grid__col
                  grid__col--8">
                  <a tabindex="0" target="_blank" href="https://safety.linkedin.com" id="globalfooter-safety_center" class="ember-view global-footer__link global-footer__link--static t-12 t-bold">
                    Safety Center
                  </a>
              </li>
          </ul>
        </nav>

        <div class="grid__col
            grid__col--12">
          <div class="grid grid--no-gutters grid--is-nested">
            <ul id="footer-action-list" class="global-footer__action-list grid__col
                grid__col--12">
                <li class="display-flex list-style-none mb4">
                  <li-icon aria-hidden="true" type="question" active="true" class="global-footer__action-icon" size="medium" color="true"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-supported-dps="24x24" fill="currentColor" class="mercado-match" width="24" height="24" focusable="false">
  <path d="M12 2a10 10 0 1010 10A10 10 0 0012 2zm0 16.25A1.25 1.25 0 1113.25 17 1.25 1.25 0 0112 18.25zm1.41-5.46L13 13v1h-2v-2.21l1.49-.79C13.82 10.34 14 9.77 14 9.3c0-.78-.92-1.3-2.3-1.3A7.12 7.12 0 008 9.24V7a8 8 0 013.7-1c3 0 4.3 1.55 4.3 3.3a3.91 3.91 0 01-2.59 3.49z"></path>
</svg></li-icon>

                  <span>
                      <a tabindex="0" target="_blank" href="https://www.linkedin.com/help/linkedin?trk=d_flagship3_profile_view_base_education_details" id="questions-help-center" class="ember-view global-footer__link global-footer__link--static t-14 t-bold">
                        Questions?
                      </a>

                    <p class="global-footer__label t-12">
                      Visit our Help Center.
                    </p>
                  </span>
                </li>
                <li class="display-flex list-style-none mb4">
                  <li-icon aria-hidden="true" type="settings" active="true" class="global-footer__action-icon" size="medium" color="true"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-supported-dps="24x24" fill="currentColor" class="mercado-match" width="24" height="24" focusable="false">
  <path d="M9.18 2l-4.3 2.52L6.22 8l-.52.91-3.7.55v5l3.64.54.54.93-1.34 3.53L9.14 22l2.29-2.9h1.09l2.3 2.9 4.32-2.52L17.79 16l.53-.93 3.68-.53v-5L18.32 9l-.51-.9 1.36-3.51L14.86 2l-2.33 3h-1zM12 9a3 3 0 11-3 3 3 3 0 013-3z"></path>
</svg></li-icon>

                  <span>
                      <a tabindex="0" target="_blank" href="https://www.linkedin.com/psettings/" id="privacy-settings" class="ember-view global-footer__link global-footer__link--static t-14 t-bold">
                        Manage your account and privacy
                      </a>

                    <p class="global-footer__label t-12">
                      Go to your Settings.
                    </p>
                  </span>
                </li>
                <li class="display-flex list-style-none mb4">
                  <li-icon aria-hidden="true" type="shield" active="true" class="global-footer__action-icon" size="medium" color="true"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" data-supported-dps="24x24" fill="currentColor" class="mercado-match" width="24" height="24" focusable="false">
  <path d="M12 4.11V19.6l-3-2a9 9 0 01-4-7.49V6.44l7-2.33M12 2L3 5v5.11a11 11 0 004.9 9.16L12 22l4.1-2.73a11 11 0 004.9-9.16V5z"></path>
</svg></li-icon>

                  <span>
                      <a tabindex="0" target="_blank" href="https://www.linkedin.com/help/linkedin/answer/a1339724" id="recommendation-transparency" class="ember-view global-footer__link global-footer__link--static t-14 t-bold">
                        Recommendation transparency
                      </a>

                    <p class="global-footer__label t-12">
                      Learn more about Recommended Content.
                    </p>
                  </span>
                </li>
            </ul>

            <div class="grid__col
                grid__col--12">
              <label for="globalfooter-select_language" class="global-footer__label t-12 t-normal mb1 mt0">
                Select Language
              </label>

              <select id="globalfooter-select_language" class="global-footer__language-selection-dropdown t-12 t-black--light t-bold">
    <option value="ar_AE" lang="ar-ae">
      العربية (Arabic)
    </option>
    <option value="cs_CZ" lang="cs-cz">
      Čeština (Czech)
    </option>
    <option value="da_DK" lang="da-dk">
      Dansk (Danish)
    </option>
    <option value="de_DE" lang="de-de">
      Deutsch (German)
    </option>
    <option value="en_US" lang="en-us">
      English (English)
    </option>
    <option value="es_ES" lang="es-es">
      Español (Spanish)
    </option>
    <option value="fr_FR" lang="fr-fr">
      Français (French)
    </option>
    <option value="hi_IN" lang="hi-in">
      हिंदी (Hindi)
    </option>
    <option value="in_ID" lang="in-id">
      Bahasa Indonesia (Indonesian)
    </option>
    <option value="it_IT" lang="it-it">
      Italiano (Italian)
    </option>
    <option value="ja_JP" lang="ja-jp">
      日本語 (Japanese)
    </option>
    <option value="ko_KR" lang="ko-kr">
      한국어 (Korean)
    </option>
    <option value="ms_MY" lang="ms-my">
      Bahasa Malaysia (Malay)
    </option>
    <option value="nl_NL" lang="nl-nl">
      Nederlands (Dutch)
    </option>
    <option value="no_NO" lang="no-no">
      Norsk (Norwegian)
    </option>
    <option value="pl_PL" lang="pl-pl">
      Polski (Polish)
    </option>
    <option value="pt_BR" lang="pt-br">
      Português (Portuguese)
    </option>
    <option value="ro_RO" lang="ro-ro">
      Română (Romanian)
    </option>
    <option value="ru_RU" lang="ru-ru">
      Русский (Russian)
    </option>
    <option value="sv_SE" lang="sv-se">
      Svenska (Swedish)
    </option>
    <option value="th_TH" lang="th-th">
      ภาษาไทย (Thai)
    </option>
    <option value="tl_PH" lang="tl-ph">
      Tagalog (Tagalog)
    </option>
    <option value="tr_TR" lang="tr-tr">
      Türkçe (Turkish)
    </option>
    <option value="uk_UA" lang="uk-ua">
      Українська (Ukrainian)
    </option>
    <option value="zh_CN" lang="zh-cn">
      简体中文 (Chinese (Simplified))
    </option>
    <option value="zh_TW" lang="zh-tw">
      正體中文 (Chinese (Traditional))
    </option>
</select>
            </div>
          </div>
        </div>
      </div>

      <p id="globalfooter-copyright" class="t-12 t-black--light t-normal text-align-left clear-both">
        LinkedIn Corporation © 2023
      </p>
    </div>
  
        </div>
  
</footer>
<!---->
  </div>
</div>
</div>

<!---->
  <!----><aside id="msg-overlay" class="msg-overlay-container msg-overlay-container-reflow
    ">
  <div tabindex="-1" class="msg-overlay-list-bubble
    
    
    ml4">
  <header class="msg-overlay-bubble-header">
    <div class="msg-overlay-bubble-header__badge-container
        "></div>
    <!---->
    <div class="msg-overlay-bubble-header__details flex-row align-items-center ml1">
      <div class="presence-entity presence-entity--size-1">
  <img src="https://media.licdn.com/dms/image/D4E03AQGB3OP3rlsmtQ/profile-displayphoto-shrink_100_100/0/1675373176223?e=1691625600&amp;v=beta&amp;t=-3k4RuOJvA8N9zuEKPE4wNyFxg7L6jKBLgCDUEe33ec" loading="lazy" alt="Harith Al-Safi" id="ember31" class="presence-entity__image EntityPhoto-circle-1  evi-image lazy-image ember-view">

    
<div class="presence-entity__indicator presence-entity__indicator--size-1
         presence-indicator
    presence-indicator--is-online
    presence-indicator--size-1">
  <span class="visually-hidden">
      Status is online
  </span>
</div>
</div>
      <button class="msg-overlay-bubble-header__button truncate ml2" type="button">
        <span class="truncate t-14 t-bold
            t-black">
          <span aria-hidden="true">
            Messaging
          </span>
          <span class="visually-hidden">
            You are on the messaging overlay. Press enter to minimize it.
          </span>
        </span>
      </button>

<!----><!---->    </div>
    <div class="msg-overlay-bubble-header__controls display-flex">
      <div id="ember32" class="artdeco-dropdown artdeco-dropdown--placement-bottom artdeco-dropdown--justification-right ember-view">
        <button aria-expanded="false" id="ember33" class="artdeco-button artdeco-button--1 artdeco-button--circle artdeco-button--muted artdeco-button--tertiary artdeco-dropdown__trigger artdeco-dropdown__trigger--placement-bottom ember-view" type="button" tabindex="0">
          <svg role="img" aria-hidden="false" aria-label="Open messenger dropdown menu" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" data-supported-dps="16x16" data-test-icon="overflow-web-ios-small">
<!---->    

    <use href="#overflow-web-ios-small" width="16" height="16"></use>
</svg>

        
<!----></button>
        <div class="msg-overlay-bubble-header__dropdown-container">
          <div tabindex="-1" aria-hidden="true" id="ember34" class="artdeco-dropdown__content artdeco-dropdown--is-dropdown-element artdeco-dropdown__content--has-arrow artdeco-dropdown__content--arrow-right artdeco-dropdown__content--justification-right artdeco-dropdown__content--placement-bottom ember-view"><!----></div>
        </div>
      </div>

      <button id="ember35" class="msg-overlay-bubble-header__control msg-overlay-bubble-header__control--new-convo-btn artdeco-button artdeco-button--circle artdeco-button--muted artdeco-button--1 artdeco-button--tertiary ember-view">  <li-icon aria-hidden="true" type="compose-icon" class="artdeco-button__icon" size="small"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" data-supported-dps="16x16" fill="currentColor" class="mercado-match" width="16" height="16" focusable="false">
  <path d="M15 2.53a1.51 1.51 0 01-.44 1L9.15 9 6 10l1-3.12 5.44-5.44A1.5 1.5 0 0115 2.53zM12 11a1 1 0 01-1 1H5a1 1 0 01-1-1V5a1 1 0 011-1h3V2H5a3 3 0 00-3 3v6a3 3 0 003 3h6a3 3 0 003-3V8h-2z"></path>
</svg></li-icon>

<span class="artdeco-button__text">
    Compose message
</span></button>

      <button id="ember36" class="msg-overlay-bubble-header__control msg-overlay-bubble-header__control--new-convo-btn artdeco-button artdeco-button--circle artdeco-button--muted artdeco-button--1 artdeco-button--tertiary ember-view">  <li-icon aria-hidden="true" type="chevron-down" class="artdeco-button__icon" size="small"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" data-supported-dps="16x16" fill="currentColor" class="mercado-match" width="16" height="16" focusable="false">
  <path d="M1 5l7 4.61L15 5v2.39L8 12 1 7.39z"></path>
</svg></li-icon>

<span class="artdeco-button__text">
    You are on the messaging overlay. Press enter to minimize it.
</span></button>
    </div>
  </header>

  <!---->

<!---->
    <div class="msg-overlay-list-bubble-search
    ">
    <div class="msg-overlay-list-bubble-search__input-container">
      <label class="a11y-text" for="msg-overlay-list-bubble-search__search-typeahead-input">
        Type to search for connections and conversations.
      </label>
      <span class="msg-overlay-list-search__search-icon display-flex">
        <svg role="none" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" data-supported-dps="16x16" data-test-icon="search-small">
<!---->    

    <use href="#search-small" width="16" height="16"></use>
</svg>

      </span>
      <input id="msg-overlay-list-bubble-search__search-typeahead-input" class="ember-text-field ember-view msg-overlay-list-bubble-search__search-typeahead-input" placeholder="Search messages" autocomplete="off" type="text">
      <div id="ember93" class="msg-overlay-list-bubble__filters-dropdown artdeco-dropdown artdeco-dropdown--placement-bottom artdeco-dropdown--justification-right ember-view">
        <button aria-expanded="false" tabindex="0" id="ember94" class="msg-overlay-list-bubble__filters-btn artdeco-dropdown__trigger artdeco-dropdown__trigger--placement-bottom ember-view" type="button">
          <li-icon type="filter-icon" size="small" role="img" aria-label="Filter messages by"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" data-supported-dps="16x16" fill="currentColor" width="16" height="16" focusable="false">
  <path d="M15 2v2H6.72a2 2 0 01-3.44 0H1V2h2.28a2 2 0 013.44 0H15zm-4 4a2 2 0 00-1.72 1H1v2h8.28a2 2 0 003.45 0H15V7h-2.28A2 2 0 0011 6zm-6 5a2 2 0 00-1.72 1H1v2h2.28a2 2 0 003.45 0H15v-2H6.72A2 2 0 005 11z"></path>
</svg></li-icon>
        
<!----></button>
        <div tabindex="-1" aria-hidden="true" id="ember95" class="artdeco-dropdown__content msg-overlay-list-bubble__filters-dropdown-content artdeco-dropdown--is-dropdown-element artdeco-dropdown__content--has-arrow artdeco-dropdown__content--arrow-right artdeco-dropdown__content--justification-right artdeco-dropdown__content--placement-bottom ember-view"><!----></div>
      </div>
    </div>

<!---->
<!---->  <div class="relative display-flex justify-center flex-column overflow-hidden
       hidden">
    <div class="msg-overlay-list-bubble-search-content">
        <div class="msg-overlay-list-bubble-search__history-placeholder-container text-align-center">
          <div class="msg-overlay-list-bubble__illustration msg-overlay-list-bubble-search__history-placeholder-illustration"></div>
          <p class="t-14 t-black t-normal ph2">
            Search your messages by recipient, content, or conversation name
          </p>
        </div>
    </div>
  </div>
</div>

    <div class="msg-overlay-list-bubble__top-static-area">
<!---->
<!---->
      <!---->
<!---->

<!---->    </div>

<!---->
<!---->
<!---->
        <section class="scrollable msg-overlay-list-bubble__content msg-overlay-list-bubble__content--scrollable">
          <div></div>
          <div class="msg-overlay-list-bubble__default-conversation-container">
<!---->
                <!---->
              <!---->
              <span class="visually-hidden">
                Attention screen reader users, messaging items continuously update. Please use the tab and shift + tab keys instead of your up and down arrow keys to navigate between messaging items.
              </span>
<!----><!---->
            <div class="msg-overlay-list-bubble__conversations-list">
        <div class="msg-conversation-listitem__link msg-overlay-list-bubble__convo-item" tabindex="0" role="button" id="overlay-conversation-card-ember97" data-feedback-redacted="">
  <div class="msg-overlay-list-bubble__convo-card-container">
    <div class="msg-conversation-card msg-overlay-list-bubble__convo-card display-flex">
      <div class="msg-selectable-entity
    
    msg-selectable-entity--3">
      <div class="presence-entity presence-entity--size-3 msg-selectable-entity__entity">
  <img src="https://media.licdn.com/dms/image/C4E03AQHRXrJo6u666A/profile-displayphoto-shrink_100_100/0/1616604610009?e=1691625600&amp;v=beta&amp;t=eC_6K7LOo7qHb3u_2OrGjH0I35w1eQKGcu0V2hE2lGs" loading="lazy" alt="Farooq Al Safi" id="ember99" class="presence-entity__image EntityPhoto-circle-3  evi-image lazy-image ember-view">

    
<div class="presence-entity__indicator presence-entity__indicator--size-3
         presence-indicator
    presence-indicator--is-reachable
    presence-indicator--size-3">
  <span class="visually-hidden">
      Status is reachable
  </span>
</div>
</div>
  <div class="msg-selectable-entity__checkbox-container">
    <input id="checkbox-msg-selectable-entity__checkbox-ember98" class="ember-checkbox ember-view msg-selectable-entity__input simple-form" type="checkbox">
    <label class="msg-selectable-entity__checkbox-label ml2" aria-label="Select conversation" for="checkbox-msg-selectable-entity__checkbox-ember98">
    </label>

    <div class="msg-selectable-entity__checkbox-circle-container">
      <div class="msg-selectable-entity__checkbox-circle">
      </div>
    </div>
  </div>
</div>

      <div class="overflow-hidden pl2
          msg-overlay-list-bubble__convo-card-content">
        <div class="msg-overlay-list-bubble__convo-card-content-wrapper fl">
          <div class="msg-conversation-card__row align-items-center display-flex">
            <h3 class="msg-conversation-listitem__participant-names msg-conversation-card__participant-names truncate t-14 t-black
                t-bold">
              Farooq Al Safi
            </h3>
            <div class="msg-conversation-card__mute-icon-holder
                msg-conversation-card__mute-icon-holder--inbox-shortcuts">
<!---->            </div>
              <time class="msg-overlay-list-bubble-item__time-stamp t-12
                  msg-overlay-list-bubble-item__time-stamp--inbox-shortcuts
                  t-bold t-black">
                Jun 6
              </time>
              <div class="msg-overlay-list-bubble__inbox-shortcuts-container">
                <div class="msg-overlay-list-bubble__inbox-shortcuts">
                  

<div id="ember100" class="artdeco-dropdown msg-thread-actions__dropdown artdeco-dropdown--placement-bottom artdeco-dropdown--justification-right ember-view">
  <button aria-expanded="false" id="ember101" class="msg-thread-actions__control artdeco-button artdeco-button--circle artdeco-button--1 artdeco-button--muted artdeco-button--tertiary artdeco-dropdown__trigger artdeco-dropdown__trigger--placement-bottom ember-view" type="button" tabindex="0">
    <li-icon aria-hidden="true" type="ellipsis-horizontal-icon" class="artdeco-button__icon" size="small" color="true"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" data-supported-dps="16x16" fill="currentColor" class="mercado-match" width="16" height="16" focusable="false">
  <path d="M3 9.5A1.5 1.5 0 114.5 8 1.5 1.5 0 013 9.5zM11.5 8A1.5 1.5 0 1013 6.5 1.5 1.5 0 0011.5 8zm-5 0A1.5 1.5 0 108 6.5 1.5 1.5 0 006.5 8z"></path>
</svg></li-icon>
    <span class="visually-hidden">
      Open the options list in your conversation with Farooq Al Safi and Harith Al-Safi
    </span>
  
<!----></button>
  <div class="msg-thread-actions__dropdown-container">
    <div tabindex="-1" aria-hidden="true" id="ember102" class="msg-thread-actions__dropdown-options--inbox-shortcuts artdeco-dropdown__content artdeco-dropdown--is-dropdown-element artdeco-dropdown__content--has-arrow artdeco-dropdown__content--arrow-right artdeco-dropdown__content--justification-right artdeco-dropdown__content--placement-bottom ember-view"><!----></div>
  </div>
</div>

<!---->

<div>
<!----></div>

<!---->
                </div>
              </div>
          </div>

          <div class="msg-conversation-card__row justify-space-between">
            <div class="msg-overlay-list-bubble__message-snippet-container--narrow-two-line">
<!---->              <p class="msg-overlay-list-bubble__message-snippet--v2
                  
                  m0 t-12
                  t-black msg-overlay-list-bubble__message-snippet--unread">
<!----><!---->                Farooq: Waaaaal
              </p>
<!---->            </div>
            <div class="display-flex">
              <div class="msg-conversation-card__conversation-status msg-conversation-card__star-icon
                  ">
<!---->              </div>
                <div class="msg-conversation-card__conversation-status align-items-center flex-grow-1">
                  <div id="ember103" class="artdeco-notification-badge ember-view msg-conversation-card__unread-count msg-conversation-card__unread-count--inbox-shortcuts artdeco-notification-badge--new text-align-center" aria-label="1 unread message">  <span class="notification-badge notification-badge--show ">
          <span aria-hidden="true" class="notification-badge__count ">1</span>
          <span class="a11y-text" data-test-notification-a11y="">1 new notification</span>
  </span>
  
                  
</div>
                </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
        <div class="msg-conversation-listitem__link msg-overlay-list-bubble__convo-item" tabindex="0" role="button" id="overlay-conversation-card-ember104" data-feedback-redacted="">
  <div class="msg-overlay-list-bubble__convo-card-container">
    <div class="msg-conversation-card msg-overlay-list-bubble__convo-card display-flex">
      <div class="msg-selectable-entity
    
    msg-selectable-entity--3">
      <div class="presence-entity presence-entity--size-3 msg-selectable-entity__entity">
  <img src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" loading="lazy" alt="Hamzah Alsafi" id="ember106" class="presence-entity__image EntityPhoto-circle-3  evi-image lazy-image ghost-person ember-view">

    
<div class="presence-entity__indicator presence-entity__indicator--size-3
         presence-indicator
    presence-indicator--is-reachable
    presence-indicator--size-3">
  <span class="visually-hidden">
      Status is reachable
  </span>
</div>
</div>
  <div class="msg-selectable-entity__checkbox-container">
    <input id="checkbox-msg-selectable-entity__checkbox-ember105" class="ember-checkbox ember-view msg-selectable-entity__input simple-form" type="checkbox">
    <label class="msg-selectable-entity__checkbox-label ml2" aria-label="Select conversation" for="checkbox-msg-selectable-entity__checkbox-ember105">
    </label>

    <div class="msg-selectable-entity__checkbox-circle-container">
      <div class="msg-selectable-entity__checkbox-circle">
      </div>
    </div>
  </div>
</div>

      <div class="overflow-hidden pl2
          msg-overlay-list-bubble__convo-card-content">
        <div class="msg-overlay-list-bubble__convo-card-content-wrapper fl">
          <div class="msg-conversation-card__row align-items-center display-flex">
            <h3 class="msg-conversation-listitem__participant-names msg-conversation-card__participant-names truncate t-14 t-black
                t-normal">
              Hamzah Alsafi
            </h3>
            <div class="msg-conversation-card__mute-icon-holder
                msg-conversation-card__mute-icon-holder--inbox-shortcuts">
<!---->            </div>
              <time class="msg-overlay-list-bubble-item__time-stamp t-12
                  msg-overlay-list-bubble-item__time-stamp--inbox-shortcuts
                  t-normal t-black--light">
                Jun 6
              </time>
              <div class="msg-overlay-list-bubble__inbox-shortcuts-container">
                <div class="msg-overlay-list-bubble__inbox-shortcuts">
                  

<div id="ember107" class="artdeco-dropdown msg-thread-actions__dropdown artdeco-dropdown--placement-bottom artdeco-dropdown--justification-right ember-view">
  <button aria-expanded="false" id="ember108" class="msg-thread-actions__control artdeco-button artdeco-button--circle artdeco-button--1 artdeco-button--muted artdeco-button--tertiary artdeco-dropdown__trigger artdeco-dropdown__trigger--placement-bottom ember-view" type="button" tabindex="0">
    <li-icon aria-hidden="true" type="ellipsis-horizontal-icon" class="artdeco-button__icon" size="small" color="true"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" data-supported-dps="16x16" fill="currentColor" class="mercado-match" width="16" height="16" focusable="false">
  <path d="M3 9.5A1.5 1.5 0 114.5 8 1.5 1.5 0 013 9.5zM11.5 8A1.5 1.5 0 1013 6.5 1.5 1.5 0 0011.5 8zm-5 0A1.5 1.5 0 108 6.5 1.5 1.5 0 006.5 8z"></path>
</svg></li-icon>
    <span class="visually-hidden">
      Open the options list in your conversation with Hamzah Alsafi and Harith Al-Safi
    </span>
  
<!----></button>
  <div class="msg-thread-actions__dropdown-container">
    <div tabindex="-1" aria-hidden="true" id="ember109" class="msg-thread-actions__dropdown-options--inbox-shortcuts artdeco-dropdown__content artdeco-dropdown--is-dropdown-element artdeco-dropdown__content--has-arrow artdeco-dropdown__content--arrow-right artdeco-dropdown__content--justification-right artdeco-dropdown__content--placement-bottom ember-view"><!----></div>
  </div>
</div>

<!---->

<div>
<!----></div>

<!---->
                </div>
              </div>
          </div>

          <div class="msg-conversation-card__row justify-space-between">
            <div class="msg-overlay-list-bubble__message-snippet-container--narrow-two-line">
<!---->              <p class="msg-overlay-list-bubble__message-snippet--v2
                  
                  m0 t-12
                  t-black--light">
<!----><!---->                You sent a post
              </p>
<!---->            </div>
            <div class="display-flex">
              <div class="msg-conversation-card__conversation-status msg-conversation-card__star-icon
                  ">
<!---->              </div>
<!---->            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
        <div class="msg-conversation-listitem__link msg-overlay-list-bubble__convo-item" tabindex="0" role="button" id="overlay-conversation-card-ember110" data-feedback-redacted="">
  <div class="msg-overlay-list-bubble__convo-card-container">
    <div class="msg-conversation-card msg-overlay-list-bubble__convo-card display-flex">
      <div class="msg-selectable-entity
    
    msg-selectable-entity--3">
      <div class="presence-entity presence-entity--size-3 msg-selectable-entity__entity">
  <img src="https://media.licdn.com/dms/image/C4E03AQFhnJjdAF9NWg/profile-displayphoto-shrink_100_100/0/1516982081020?e=1691625600&amp;v=beta&amp;t=U3jhj62NIQAqc0UVuhPmmul60UFXmyNy0LfTAqIA-d0" loading="lazy" alt="Ausama Al Safi" id="ember112" class="presence-entity__image EntityPhoto-circle-3  evi-image lazy-image ember-view">

    
<div class="presence-entity__indicator presence-entity__indicator--size-3
         presence-indicator
    presence-indicator--is-reachable
    presence-indicator--size-3">
  <span class="visually-hidden">
      Status is reachable
  </span>
</div>
</div>
  <div class="msg-selectable-entity__checkbox-container">
    <input id="checkbox-msg-selectable-entity__checkbox-ember111" class="ember-checkbox ember-view msg-selectable-entity__input simple-form" type="checkbox">
    <label class="msg-selectable-entity__checkbox-label ml2" aria-label="Select conversation" for="checkbox-msg-selectable-entity__checkbox-ember111">
    </label>

    <div class="msg-selectable-entity__checkbox-circle-container">
      <div class="msg-selectable-entity__checkbox-circle">
      </div>
    </div>
  </div>
</div>

      <div class="overflow-hidden pl2
          msg-overlay-list-bubble__convo-card-content">
        <div class="msg-overlay-list-bubble__convo-card-content-wrapper fl">
          <div class="msg-conversation-card__row align-items-center display-flex">
            <h3 class="msg-conversation-listitem__participant-names msg-conversation-card__participant-names truncate t-14 t-black
                t-bold">
              Ausama Al Safi
            </h3>
            <div class="msg-conversation-card__mute-icon-holder
                msg-conversation-card__mute-icon-holder--inbox-shortcuts">
<!---->            </div>
              <time class="msg-overlay-list-bubble-item__time-stamp t-12
                  msg-overlay-list-bubble-item__time-stamp--inbox-shortcuts
                  t-bold t-black">
                Jun 5
              </time>
              <div class="msg-overlay-list-bubble__inbox-shortcuts-container">
                <div class="msg-overlay-list-bubble__inbox-shortcuts">
                  

<div id="ember113" class="artdeco-dropdown msg-thread-actions__dropdown artdeco-dropdown--placement-bottom artdeco-dropdown--justification-right ember-view">
  <button aria-expanded="false" id="ember114" class="msg-thread-actions__control artdeco-button artdeco-button--circle artdeco-button--1 artdeco-button--muted artdeco-button--tertiary artdeco-dropdown__trigger artdeco-dropdown__trigger--placement-bottom ember-view" type="button" tabindex="0">
    <li-icon aria-hidden="true" type="ellipsis-horizontal-icon" class="artdeco-button__icon" size="small" color="true"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" data-supported-dps="16x16" fill="currentColor" class="mercado-match" width="16" height="16" focusable="false">
  <path d="M3 9.5A1.5 1.5 0 114.5 8 1.5 1.5 0 013 9.5zM11.5 8A1.5 1.5 0 1013 6.5 1.5 1.5 0 0011.5 8zm-5 0A1.5 1.5 0 108 6.5 1.5 1.5 0 006.5 8z"></path>
</svg></li-icon>
    <span class="visually-hidden">
      Open the options list in your conversation with Harith Al-Safi and Ausama Al Safi
    </span>
  
<!----></button>
  <div class="msg-thread-actions__dropdown-container">
    <div tabindex="-1" aria-hidden="true" id="ember115" class="msg-thread-actions__dropdown-options--inbox-shortcuts artdeco-dropdown__content artdeco-dropdown--is-dropdown-element artdeco-dropdown__content--has-arrow artdeco-dropdown__content--arrow-right artdeco-dropdown__content--justification-right artdeco-dropdown__content--placement-bottom ember-view"><!----></div>
  </div>
</div>

<!---->

<div>
<!----></div>

<!---->
                </div>
              </div>
          </div>

          <div class="msg-conversation-card__row justify-space-between">
            <div class="msg-overlay-list-bubble__message-snippet-container--narrow-two-line">
<!---->              <p class="msg-overlay-list-bubble__message-snippet--v2
                  
                  m0 t-12
                  t-black msg-overlay-list-bubble__message-snippet--unread">
<!----><!---->                Ausama: Thanks
              </p>
<!---->            </div>
            <div class="display-flex">
              <div class="msg-conversation-card__conversation-status msg-conversation-card__star-icon
                  ">
<!---->              </div>
                <div class="msg-conversation-card__conversation-status align-items-center flex-grow-1">
                  <div id="ember116" class="artdeco-notification-badge ember-view msg-conversation-card__unread-count msg-conversation-card__unread-count--inbox-shortcuts artdeco-notification-badge--new text-align-center" aria-label="1 unread message">  <span class="notification-badge notification-badge--show ">
          <span aria-hidden="true" class="notification-badge__count ">1</span>
          <span class="a11y-text" data-test-notification-a11y="">1 new notification</span>
  </span>
  
                  
</div>
                </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
        <div class="msg-conversation-listitem__link msg-overlay-list-bubble__convo-item" tabindex="0" role="button" id="overlay-conversation-card-ember117" data-feedback-redacted="">
  <div class="msg-overlay-list-bubble__convo-card-container">
    <div class="msg-conversation-card msg-overlay-list-bubble__convo-card display-flex">
      <div class="msg-selectable-entity
    
    msg-selectable-entity--3">
      <div class="presence-entity presence-entity--size-3 msg-selectable-entity__entity">
  <img src="https://media.licdn.com/dms/image/D4E03AQGQznKmDE2xrA/profile-displayphoto-shrink_100_100/0/1674598855086?e=1691625600&amp;v=beta&amp;t=fQzPqpxhsh6kamZA306xn-vjQ80SIMIgi6A0dPCRmhw" loading="lazy" alt="Harith Ibrahim" id="ember119" class="presence-entity__image EntityPhoto-circle-3  evi-image lazy-image ember-view">

    
<div class="presence-entity__indicator presence-entity__indicator--size-3
         presence-indicator
    presence-indicator--is-online
    presence-indicator--size-3">
  <span class="visually-hidden">
      Status is online
  </span>
</div>
</div>
  <div class="msg-selectable-entity__checkbox-container">
    <input id="checkbox-msg-selectable-entity__checkbox-ember118" class="ember-checkbox ember-view msg-selectable-entity__input simple-form" type="checkbox">
    <label class="msg-selectable-entity__checkbox-label ml2" aria-label="Select conversation" for="checkbox-msg-selectable-entity__checkbox-ember118">
    </label>

    <div class="msg-selectable-entity__checkbox-circle-container">
      <div class="msg-selectable-entity__checkbox-circle">
      </div>
    </div>
  </div>
</div>

      <div class="overflow-hidden pl2
          msg-overlay-list-bubble__convo-card-content">
        <div class="msg-overlay-list-bubble__convo-card-content-wrapper fl">
          <div class="msg-conversation-card__row align-items-center display-flex">
            <h3 class="msg-conversation-listitem__participant-names msg-conversation-card__participant-names truncate t-14 t-black
                t-normal">
              Harith Ibrahim
            </h3>
            <div class="msg-conversation-card__mute-icon-holder
                msg-conversation-card__mute-icon-holder--inbox-shortcuts">
<!---->            </div>
              <time class="msg-overlay-list-bubble-item__time-stamp t-12
                  msg-overlay-list-bubble-item__time-stamp--inbox-shortcuts
                  t-normal t-black--light">
                Jun 5
              </time>
              <div class="msg-overlay-list-bubble__inbox-shortcuts-container">
                <div class="msg-overlay-list-bubble__inbox-shortcuts">
                  

<div id="ember120" class="artdeco-dropdown msg-thread-actions__dropdown artdeco-dropdown--placement-bottom artdeco-dropdown--justification-right ember-view">
  <button aria-expanded="false" id="ember121" class="msg-thread-actions__control artdeco-button artdeco-button--circle artdeco-button--1 artdeco-button--muted artdeco-button--tertiary artdeco-dropdown__trigger artdeco-dropdown__trigger--placement-bottom ember-view" type="button" tabindex="0">
    <li-icon aria-hidden="true" type="ellipsis-horizontal-icon" class="artdeco-button__icon" size="small" color="true"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" data-supported-dps="16x16" fill="currentColor" class="mercado-match" width="16" height="16" focusable="false">
  <path d="M3 9.5A1.5 1.5 0 114.5 8 1.5 1.5 0 013 9.5zM11.5 8A1.5 1.5 0 1013 6.5 1.5 1.5 0 0011.5 8zm-5 0A1.5 1.5 0 108 6.5 1.5 1.5 0 006.5 8z"></path>
</svg></li-icon>
    <span class="visually-hidden">
      Open the options list in your conversation with Harith Ibrahim and Harith Al-Safi
    </span>
  
<!----></button>
  <div class="msg-thread-actions__dropdown-container">
    <div tabindex="-1" aria-hidden="true" id="ember122" class="msg-thread-actions__dropdown-options--inbox-shortcuts artdeco-dropdown__content artdeco-dropdown--is-dropdown-element artdeco-dropdown__content--has-arrow artdeco-dropdown__content--arrow-right artdeco-dropdown__content--justification-right artdeco-dropdown__content--placement-bottom ember-view"><!----></div>
  </div>
</div>

<!---->

<div>
<!----></div>

<!---->
                </div>
              </div>
          </div>

          <div class="msg-conversation-card__row justify-space-between">
            <div class="msg-overlay-list-bubble__message-snippet-container--narrow-two-line">
<!---->              <p class="msg-overlay-list-bubble__message-snippet--v2
                  
                  m0 t-12
                  t-black--light">
<!----><!---->                You sent a post
              </p>
<!---->            </div>
            <div class="display-flex">
              <div class="msg-conversation-card__conversation-status msg-conversation-card__star-icon
                  ">
<!---->              </div>
<!---->            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
        <div class="msg-conversation-listitem__link msg-overlay-list-bubble__convo-item" tabindex="0" role="button" id="overlay-conversation-card-ember123" data-feedback-redacted="">
  <div class="msg-overlay-list-bubble__convo-card-container">
    <div class="msg-conversation-card msg-overlay-list-bubble__convo-card display-flex">
      <div class="msg-selectable-entity
    
    msg-selectable-entity--3">
      <div class="presence-entity presence-entity--size-3 msg-selectable-entity__entity">
  <img src="https://media.licdn.com/dms/image/C4E03AQFHqAJ1vvzJxQ/profile-displayphoto-shrink_100_100/0/1659203750179?e=1691625600&amp;v=beta&amp;t=IFUHS3oP9rwYv432iMmFGgAGSB6JGQIOc82KdaLl7HE" loading="lazy" alt="Hamidulhassan Khan" id="ember125" class="presence-entity__image EntityPhoto-circle-3  evi-image lazy-image ember-view">

    
<div class="presence-entity__indicator presence-entity__indicator--size-3
         presence-indicator
    presence-indicator--is-reachable
    presence-indicator--size-3">
  <span class="visually-hidden">
      Status is reachable
  </span>
</div>
</div>
  <div class="msg-selectable-entity__checkbox-container">
    <input id="checkbox-msg-selectable-entity__checkbox-ember124" class="ember-checkbox ember-view msg-selectable-entity__input simple-form" type="checkbox">
    <label class="msg-selectable-entity__checkbox-label ml2" aria-label="Select conversation" for="checkbox-msg-selectable-entity__checkbox-ember124">
    </label>

    <div class="msg-selectable-entity__checkbox-circle-container">
      <div class="msg-selectable-entity__checkbox-circle">
      </div>
    </div>
  </div>
</div>

      <div class="overflow-hidden pl2
          msg-overlay-list-bubble__convo-card-content">
        <div class="msg-overlay-list-bubble__convo-card-content-wrapper fl">
          <div class="msg-conversation-card__row align-items-center display-flex">
            <h3 class="msg-conversation-listitem__participant-names msg-conversation-card__participant-names truncate t-14 t-black
                t-bold">
              Hamidulhassan Khan
            </h3>
            <div class="msg-conversation-card__mute-icon-holder
                msg-conversation-card__mute-icon-holder--inbox-shortcuts">
<!---->            </div>
              <time class="msg-overlay-list-bubble-item__time-stamp t-12
                  msg-overlay-list-bubble-item__time-stamp--inbox-shortcuts
                  t-bold t-black">
                Jun 3
              </time>
              <div class="msg-overlay-list-bubble__inbox-shortcuts-container">
                <div class="msg-overlay-list-bubble__inbox-shortcuts">
                  

<div id="ember126" class="artdeco-dropdown msg-thread-actions__dropdown artdeco-dropdown--placement-bottom artdeco-dropdown--justification-right ember-view">
  <button aria-expanded="false" id="ember127" class="msg-thread-actions__control artdeco-button artdeco-button--circle artdeco-button--1 artdeco-button--muted artdeco-button--tertiary artdeco-dropdown__trigger artdeco-dropdown__trigger--placement-bottom ember-view" type="button" tabindex="0">
    <li-icon aria-hidden="true" type="ellipsis-horizontal-icon" class="artdeco-button__icon" size="small" color="true"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" data-supported-dps="16x16" fill="currentColor" class="mercado-match" width="16" height="16" focusable="false">
  <path d="M3 9.5A1.5 1.5 0 114.5 8 1.5 1.5 0 013 9.5zM11.5 8A1.5 1.5 0 1013 6.5 1.5 1.5 0 0011.5 8zm-5 0A1.5 1.5 0 108 6.5 1.5 1.5 0 006.5 8z"></path>
</svg></li-icon>
    <span class="visually-hidden">
      Open the options list in your conversation with Harith Al-Safi and Hamidulhassan Khan
    </span>
  
<!----></button>
  <div class="msg-thread-actions__dropdown-container">
    <div tabindex="-1" aria-hidden="true" id="ember128" class="msg-thread-actions__dropdown-options--inbox-shortcuts artdeco-dropdown__content artdeco-dropdown--is-dropdown-element artdeco-dropdown__content--has-arrow artdeco-dropdown__content--arrow-right artdeco-dropdown__content--justification-right artdeco-dropdown__content--placement-bottom ember-view"><!----></div>
  </div>
</div>

<!---->

<div>
<!----></div>

<!---->
                </div>
              </div>
          </div>

          <div class="msg-conversation-card__row justify-space-between">
            <div class="msg-overlay-list-bubble__message-snippet-container--narrow-two-line">
<!---->              <p class="msg-overlay-list-bubble__message-snippet--v2
                  
                  m0 t-12
                  t-black msg-overlay-list-bubble__message-snippet--unread">
<!----><!---->                Hamidulhassan: I am keen to meet you ;)
              </p>
<!---->            </div>
            <div class="display-flex">
              <div class="msg-conversation-card__conversation-status msg-conversation-card__star-icon
                  ">
<!---->              </div>
                <div class="msg-conversation-card__conversation-status align-items-center flex-grow-1">
                  <div id="ember129" class="artdeco-notification-badge ember-view msg-conversation-card__unread-count msg-conversation-card__unread-count--inbox-shortcuts artdeco-notification-badge--new text-align-center" aria-label="1 unread message">  <span class="notification-badge notification-badge--show ">
          <span aria-hidden="true" class="notification-badge__count ">1</span>
          <span class="a11y-text" data-test-notification-a11y="">1 new notification</span>
  </span>
  
                  
</div>
                </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
        <div class="msg-conversation-listitem__link msg-overlay-list-bubble__convo-item" tabindex="0" role="button" id="overlay-conversation-card-ember130" data-feedback-redacted="">
  <div class="msg-overlay-list-bubble__convo-card-container">
    <div class="msg-conversation-card msg-overlay-list-bubble__convo-card display-flex">
      <div class="msg-selectable-entity
    
    msg-selectable-entity--3">
      <div class="presence-entity presence-entity--size-3 msg-selectable-entity__entity">
  <img src="https://media.licdn.com/dms/image/D4E03AQEMwPaA-IvI1A/profile-displayphoto-shrink_100_100/0/1669672329465?e=1691625600&amp;v=beta&amp;t=kXxnSyTFv0siSOvQ5VQn0jY-jhTeglb1GJgdYX-WMb0" loading="lazy" alt="Sam Eve" id="ember132" class="presence-entity__image EntityPhoto-circle-3  evi-image lazy-image ember-view">

    
<div class="presence-entity__indicator presence-entity__indicator--size-3
         presence-indicator
    presence-indicator--is-online
    presence-indicator--size-3">
  <span class="visually-hidden">
      Status is online
  </span>
</div>
</div>
  <div class="msg-selectable-entity__checkbox-container">
    <input id="checkbox-msg-selectable-entity__checkbox-ember131" class="ember-checkbox ember-view msg-selectable-entity__input simple-form" type="checkbox">
    <label class="msg-selectable-entity__checkbox-label ml2" aria-label="Select conversation" for="checkbox-msg-selectable-entity__checkbox-ember131">
    </label>

    <div class="msg-selectable-entity__checkbox-circle-container">
      <div class="msg-selectable-entity__checkbox-circle">
      </div>
    </div>
  </div>
</div>

      <div class="overflow-hidden pl2
          msg-overlay-list-bubble__convo-card-content">
        <div class="msg-overlay-list-bubble__convo-card-content-wrapper fl">
          <div class="msg-conversation-card__row align-items-center display-flex">
            <h3 class="msg-conversation-listitem__participant-names msg-conversation-card__participant-names truncate t-14 t-black
                t-normal">
              Sam Eve
            </h3>
            <div class="msg-conversation-card__mute-icon-holder
                msg-conversation-card__mute-icon-holder--inbox-shortcuts">
<!---->            </div>
              <time class="msg-overlay-list-bubble-item__time-stamp t-12
                  msg-overlay-list-bubble-item__time-stamp--inbox-shortcuts
                  t-normal t-black--light">
                Jun 1
              </time>
              <div class="msg-overlay-list-bubble__inbox-shortcuts-container">
                <div class="msg-overlay-list-bubble__inbox-shortcuts">
                  

<div id="ember133" class="artdeco-dropdown msg-thread-actions__dropdown artdeco-dropdown--placement-bottom artdeco-dropdown--justification-right ember-view">
  <button aria-expanded="false" id="ember134" class="msg-thread-actions__control artdeco-button artdeco-button--circle artdeco-button--1 artdeco-button--muted artdeco-button--tertiary artdeco-dropdown__trigger artdeco-dropdown__trigger--placement-bottom ember-view" type="button" tabindex="0">
    <li-icon aria-hidden="true" type="ellipsis-horizontal-icon" class="artdeco-button__icon" size="small" color="true"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" data-supported-dps="16x16" fill="currentColor" class="mercado-match" width="16" height="16" focusable="false">
  <path d="M3 9.5A1.5 1.5 0 114.5 8 1.5 1.5 0 013 9.5zM11.5 8A1.5 1.5 0 1013 6.5 1.5 1.5 0 0011.5 8zm-5 0A1.5 1.5 0 108 6.5 1.5 1.5 0 006.5 8z"></path>
</svg></li-icon>
    <span class="visually-hidden">
      Open the options list in your conversation with Harith Al-Safi and Sam Eve
    </span>
  
<!----></button>
  <div class="msg-thread-actions__dropdown-container">
    <div tabindex="-1" aria-hidden="true" id="ember135" class="msg-thread-actions__dropdown-options--inbox-shortcuts artdeco-dropdown__content artdeco-dropdown--is-dropdown-element artdeco-dropdown__content--has-arrow artdeco-dropdown__content--arrow-right artdeco-dropdown__content--justification-right artdeco-dropdown__content--placement-bottom ember-view"><!----></div>
  </div>
</div>

<!---->

<div>
<!----></div>

<!---->
                </div>
              </div>
          </div>

          <div class="msg-conversation-card__row justify-space-between">
            <div class="msg-overlay-list-bubble__message-snippet-container--narrow-two-line">
<!---->              <p class="msg-overlay-list-bubble__message-snippet--v2
                  
                  m0 t-12
                  t-black--light">
<!----><!---->                You: just posted a comment on it :)
              </p>
<!---->            </div>
            <div class="display-flex">
              <div class="msg-conversation-card__conversation-status msg-conversation-card__star-icon
                  ">
<!---->              </div>
<!---->            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
        <div class="msg-conversation-listitem__link msg-overlay-list-bubble__convo-item" tabindex="0" role="button" id="overlay-conversation-card-ember136" data-feedback-redacted="">
  <div class="msg-overlay-list-bubble__convo-card-container">
    <div class="msg-conversation-card msg-overlay-list-bubble__convo-card display-flex">
      <div class="msg-selectable-entity
    
    msg-selectable-entity--3">
      <div class="presence-entity presence-entity--size-3 msg-selectable-entity__entity">
  <img src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" loading="lazy" alt="Dean Lynch" id="ember138" class="presence-entity__image EntityPhoto-circle-3  evi-image lazy-image ghost-person ember-view">

    
<div class="presence-entity__indicator presence-entity__indicator--size-3
         presence-indicator
    hidden
    presence-indicator--size-3">
  <span class="visually-hidden">
      Status is offline
      </span>
</div>
</div>
  <div class="msg-selectable-entity__checkbox-container">
    <input id="checkbox-msg-selectable-entity__checkbox-ember137" class="ember-checkbox ember-view msg-selectable-entity__input simple-form" type="checkbox">
    <label class="msg-selectable-entity__checkbox-label ml2" aria-label="Select conversation" for="checkbox-msg-selectable-entity__checkbox-ember137">
    </label>

    <div class="msg-selectable-entity__checkbox-circle-container">
      <div class="msg-selectable-entity__checkbox-circle">
      </div>
    </div>
  </div>
</div>

      <div class="overflow-hidden pl2
          msg-overlay-list-bubble__convo-card-content">
        <div class="msg-overlay-list-bubble__convo-card-content-wrapper fl">
          <div class="msg-conversation-card__row align-items-center display-flex">
            <h3 class="msg-conversation-listitem__participant-names msg-conversation-card__participant-names truncate t-14 t-black
                t-normal">
              Dean Lynch
            </h3>
            <div class="msg-conversation-card__mute-icon-holder
                msg-conversation-card__mute-icon-holder--inbox-shortcuts">
<!---->            </div>
              <time class="msg-overlay-list-bubble-item__time-stamp t-12
                  msg-overlay-list-bubble-item__time-stamp--inbox-shortcuts
                  t-normal t-black--light">
                May 31
              </time>
              <div class="msg-overlay-list-bubble__inbox-shortcuts-container">
                <div class="msg-overlay-list-bubble__inbox-shortcuts">
                  

<div id="ember139" class="artdeco-dropdown msg-thread-actions__dropdown artdeco-dropdown--placement-bottom artdeco-dropdown--justification-right ember-view">
  <button aria-expanded="false" id="ember140" class="msg-thread-actions__control artdeco-button artdeco-button--circle artdeco-button--1 artdeco-button--muted artdeco-button--tertiary artdeco-dropdown__trigger artdeco-dropdown__trigger--placement-bottom ember-view" type="button" tabindex="0">
    <li-icon aria-hidden="true" type="ellipsis-horizontal-icon" class="artdeco-button__icon" size="small" color="true"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" data-supported-dps="16x16" fill="currentColor" class="mercado-match" width="16" height="16" focusable="false">
  <path d="M3 9.5A1.5 1.5 0 114.5 8 1.5 1.5 0 013 9.5zM11.5 8A1.5 1.5 0 1013 6.5 1.5 1.5 0 0011.5 8zm-5 0A1.5 1.5 0 108 6.5 1.5 1.5 0 006.5 8z"></path>
</svg></li-icon>
    <span class="visually-hidden">
      Open the options list in your conversation with Harith Al-Safi and Dean Lynch
    </span>
  
<!----></button>
  <div class="msg-thread-actions__dropdown-container">
    <div tabindex="-1" aria-hidden="true" id="ember141" class="msg-thread-actions__dropdown-options--inbox-shortcuts artdeco-dropdown__content artdeco-dropdown--is-dropdown-element artdeco-dropdown__content--has-arrow artdeco-dropdown__content--arrow-right artdeco-dropdown__content--justification-right artdeco-dropdown__content--placement-bottom ember-view"><!----></div>
  </div>
</div>

<!---->

<div>
<!----></div>

<!---->
                </div>
              </div>
          </div>

          <div class="msg-conversation-card__row justify-space-between">
            <div class="msg-overlay-list-bubble__message-snippet-container--narrow-two-line">
<!---->              <p class="msg-overlay-list-bubble__message-snippet--v2
                  
                  m0 t-12
                  t-black--light">
<!----><!---->                You: I think so yess
              </p>
<!---->            </div>
            <div class="display-flex">
              <div class="msg-conversation-card__conversation-status msg-conversation-card__star-icon
                  ">
<!---->              </div>
<!---->            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
        <div class="msg-conversation-listitem__link msg-overlay-list-bubble__convo-item" tabindex="0" role="button" id="overlay-conversation-card-ember142" data-feedback-redacted="">
  <div class="msg-overlay-list-bubble__convo-card-container">
    <div class="msg-conversation-card msg-overlay-list-bubble__convo-card display-flex">
      <div class="msg-selectable-entity
    
    msg-selectable-entity--3">
      <div class="msg-facepile-grid--no-facepile msg-facepile-grid
    msg-facepile-grid--3 msg-selectable-entity__entity">
<!---->      <img src="https://media.licdn.com/dms/image/C560BAQEWL3x6YrK4TQ/company-logo_100_100/0/1612473028270?e=1694044800&amp;v=beta&amp;t=Gh0T71xnVBUoRb6-rsPiRKurr1N9dgvWVyPt4KElz5I" loading="lazy" alt="LinkedIn Learning" id="ember230" class="evi-image lazy-image msg-facepile-grid__img msg-facepile-grid__img--company ember-view">
</div>
      <div class="msg-selectable-entity__checkbox-container">
    <input id="checkbox-msg-selectable-entity__checkbox-ember143" class="ember-checkbox ember-view msg-selectable-entity__input simple-form" type="checkbox">
    <label class="msg-selectable-entity__checkbox-label ml2" aria-label="Select conversation" for="checkbox-msg-selectable-entity__checkbox-ember143">
    </label>

    <div class="msg-selectable-entity__checkbox-circle-container">
      <div class="msg-selectable-entity__checkbox-circle">
      </div>
    </div>
  </div>
</div>

      <div class="overflow-hidden pl2
          msg-overlay-list-bubble__convo-card-content">
        <div class="msg-overlay-list-bubble__convo-card-content-wrapper fl">
          <div class="msg-conversation-card__row align-items-center display-flex">
            <h3 class="msg-conversation-listitem__participant-names msg-conversation-card__participant-names truncate t-14 t-black
                t-normal">
              LinkedIn Learning
            </h3>
            <div class="msg-conversation-card__mute-icon-holder
                msg-conversation-card__mute-icon-holder--inbox-shortcuts">
<!---->            </div>
              <time class="msg-overlay-list-bubble-item__time-stamp t-12
                  msg-overlay-list-bubble-item__time-stamp--inbox-shortcuts
                  t-normal t-black--light">
                May 23
              </time>
              <div class="msg-overlay-list-bubble__inbox-shortcuts-container">
                <div class="msg-overlay-list-bubble__inbox-shortcuts">
                  

<div id="ember145" class="artdeco-dropdown msg-thread-actions__dropdown artdeco-dropdown--placement-bottom artdeco-dropdown--justification-right ember-view">
  <button aria-expanded="false" id="ember146" class="msg-thread-actions__control artdeco-button artdeco-button--circle artdeco-button--1 artdeco-button--muted artdeco-button--tertiary artdeco-dropdown__trigger artdeco-dropdown__trigger--placement-bottom ember-view" type="button" tabindex="0">
    <li-icon aria-hidden="true" type="ellipsis-horizontal-icon" class="artdeco-button__icon" size="small" color="true"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" data-supported-dps="16x16" fill="currentColor" class="mercado-match" width="16" height="16" focusable="false">
  <path d="M3 9.5A1.5 1.5 0 114.5 8 1.5 1.5 0 013 9.5zM11.5 8A1.5 1.5 0 1013 6.5 1.5 1.5 0 0011.5 8zm-5 0A1.5 1.5 0 108 6.5 1.5 1.5 0 006.5 8z"></path>
</svg></li-icon>
    <span class="visually-hidden">
      Open the options list in your conversation with LinkedIn Learning
    </span>
  
<!----></button>
  <div class="msg-thread-actions__dropdown-container">
    <div tabindex="-1" aria-hidden="true" id="ember147" class="msg-thread-actions__dropdown-options--inbox-shortcuts artdeco-dropdown__content artdeco-dropdown--is-dropdown-element artdeco-dropdown__content--has-arrow artdeco-dropdown__content--arrow-right artdeco-dropdown__content--justification-right artdeco-dropdown__content--placement-bottom ember-view"><!----></div>
  </div>
</div>

<!---->

<div>
<!----></div>

<!---->
                </div>
              </div>
          </div>

          <div class="msg-conversation-card__row justify-space-between">
            <div class="msg-overlay-list-bubble__message-snippet-container--narrow-two-line">
<!---->              <p class="msg-overlay-list-bubble__message-snippet--v2
                  
                  m0 t-12
                  t-black--light">
<!---->                  <span class="msg-conversation-card__pill t-14
                       t-black 
                      t-bold pr1">
                    LinkedIn Offer
                  </span>
                Hi Harith,

We'd like to invite you to try LinkedIn Learning free for one month. Whether you’re growing your career, job seeking, or leading a team, LinkedIn Learning has relevant on-demand courses to help you keep learning in the moments that matter.
              </p>
<!---->            </div>
            <div class="display-flex">
              <div class="msg-conversation-card__conversation-status msg-conversation-card__star-icon
                  ">
<!---->              </div>
<!---->            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
        <div class="msg-conversation-listitem__link msg-overlay-list-bubble__convo-item" tabindex="0" role="button" id="overlay-conversation-card-ember148" data-feedback-redacted="">
  <div class="msg-overlay-list-bubble__convo-card-container">
    <div class="msg-conversation-card msg-overlay-list-bubble__convo-card display-flex">
      <div class="msg-selectable-entity
    
    msg-selectable-entity--3">
      <div class="msg-facepile-grid--no-facepile msg-facepile-grid
    msg-facepile-grid--3 msg-selectable-entity__entity">
<!---->      <img src="https://media.licdn.com/dms/image/C5603AQFjN6ojx2xLqQ/profile-displayphoto-shrink_100_100/0/1639790308016?e=1691625600&amp;v=beta&amp;t=R3w6AIzMMnMg3_r-qnazt9DZ0lUz6R8hEf2lu7ltEWs" loading="lazy" alt="Dani Schenone, MBA, RYT, ACSM-CPT" id="ember231" class="evi-image lazy-image msg-facepile-grid__img msg-facepile-grid__img--person ember-view">
</div>
      <div class="msg-selectable-entity__checkbox-container">
    <input id="checkbox-msg-selectable-entity__checkbox-ember149" class="ember-checkbox ember-view msg-selectable-entity__input simple-form" type="checkbox">
    <label class="msg-selectable-entity__checkbox-label ml2" aria-label="Select conversation" for="checkbox-msg-selectable-entity__checkbox-ember149">
    </label>

    <div class="msg-selectable-entity__checkbox-circle-container">
      <div class="msg-selectable-entity__checkbox-circle">
      </div>
    </div>
  </div>
</div>

      <div class="overflow-hidden pl2
          msg-overlay-list-bubble__convo-card-content">
        <div class="msg-overlay-list-bubble__convo-card-content-wrapper fl">
          <div class="msg-conversation-card__row align-items-center display-flex">
            <h3 class="msg-conversation-listitem__participant-names msg-conversation-card__participant-names truncate t-14 t-black
                t-normal">
              Dani Schenone, MBA, RYT, ACSM-CPT
            </h3>
            <div class="msg-conversation-card__mute-icon-holder
                msg-conversation-card__mute-icon-holder--inbox-shortcuts">
<!---->            </div>
              <time class="msg-overlay-list-bubble-item__time-stamp t-12
                  msg-overlay-list-bubble-item__time-stamp--inbox-shortcuts
                  t-normal t-black--light">
                May 18
              </time>
              <div class="msg-overlay-list-bubble__inbox-shortcuts-container">
                <div class="msg-overlay-list-bubble__inbox-shortcuts">
                  

<div id="ember151" class="artdeco-dropdown msg-thread-actions__dropdown artdeco-dropdown--placement-bottom artdeco-dropdown--justification-right ember-view">
  <button aria-expanded="false" id="ember152" class="msg-thread-actions__control artdeco-button artdeco-button--circle artdeco-button--1 artdeco-button--muted artdeco-button--tertiary artdeco-dropdown__trigger artdeco-dropdown__trigger--placement-bottom ember-view" type="button" tabindex="0">
    <li-icon aria-hidden="true" type="ellipsis-horizontal-icon" class="artdeco-button__icon" size="small" color="true"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" data-supported-dps="16x16" fill="currentColor" class="mercado-match" width="16" height="16" focusable="false">
  <path d="M3 9.5A1.5 1.5 0 114.5 8 1.5 1.5 0 013 9.5zM11.5 8A1.5 1.5 0 1013 6.5 1.5 1.5 0 0011.5 8zm-5 0A1.5 1.5 0 108 6.5 1.5 1.5 0 006.5 8z"></path>
</svg></li-icon>
    <span class="visually-hidden">
      Open the options list in your conversation with Dani Schenone, MBA, RYT, ACSM-CPT
    </span>
  
<!----></button>
  <div class="msg-thread-actions__dropdown-container">
    <div tabindex="-1" aria-hidden="true" id="ember153" class="msg-thread-actions__dropdown-options--inbox-shortcuts artdeco-dropdown__content artdeco-dropdown--is-dropdown-element artdeco-dropdown__content--has-arrow artdeco-dropdown__content--arrow-right artdeco-dropdown__content--justification-right artdeco-dropdown__content--placement-bottom ember-view"><!----></div>
  </div>
</div>

<!---->

<div>
<!----></div>

<!---->
                </div>
              </div>
          </div>

          <div class="msg-conversation-card__row justify-space-between">
            <div class="msg-overlay-list-bubble__message-snippet-container--narrow-two-line">
<!---->              <p class="msg-overlay-list-bubble__message-snippet--v2
                  
                  m0 t-12
                  t-black--light">
<!---->                  <span class="msg-conversation-card__pill t-14
                       t-black 
                      t-bold pr1">
                    Sponsored
                  </span>
                Great! I hope you will find it interesting! We have a ton of other resources on the website.
              </p>
<!---->            </div>
            <div class="display-flex">
              <div class="msg-conversation-card__conversation-status msg-conversation-card__star-icon
                  ">
<!---->              </div>
<!---->            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
        <div class="msg-conversation-listitem__link msg-overlay-list-bubble__convo-item" tabindex="0" role="button" id="overlay-conversation-card-ember154" data-feedback-redacted="">
  <div class="msg-overlay-list-bubble__convo-card-container">
    <div class="msg-conversation-card msg-overlay-list-bubble__convo-card display-flex">
      <div class="msg-selectable-entity
    
    msg-selectable-entity--3">
      <div class="presence-entity presence-entity--size-3 msg-selectable-entity__entity">
  <img src="https://media.licdn.com/dms/image/D4E03AQFrgm1knSbr1Q/profile-displayphoto-shrink_100_100/0/1673895470425?e=1691625600&amp;v=beta&amp;t=bCmszktoOc6SxoWm7Q9wIvN5VtsYdJR24zugb012E1A" loading="lazy" alt="Russell Gillespie" id="ember156" class="presence-entity__image EntityPhoto-circle-3  evi-image lazy-image ember-view">

    
<div class="presence-entity__indicator presence-entity__indicator--size-3
         presence-indicator
    hidden
    presence-indicator--size-3">
  <span class="visually-hidden">
      Status is offline
      </span>
</div>
</div>
  <div class="msg-selectable-entity__checkbox-container">
    <input id="checkbox-msg-selectable-entity__checkbox-ember155" class="ember-checkbox ember-view msg-selectable-entity__input simple-form" type="checkbox">
    <label class="msg-selectable-entity__checkbox-label ml2" aria-label="Select conversation" for="checkbox-msg-selectable-entity__checkbox-ember155">
    </label>

    <div class="msg-selectable-entity__checkbox-circle-container">
      <div class="msg-selectable-entity__checkbox-circle">
      </div>
    </div>
  </div>
</div>

      <div class="overflow-hidden pl2
          msg-overlay-list-bubble__convo-card-content">
        <div class="msg-overlay-list-bubble__convo-card-content-wrapper fl">
          <div class="msg-conversation-card__row align-items-center display-flex">
            <h3 class="msg-conversation-listitem__participant-names msg-conversation-card__participant-names truncate t-14 t-black
                t-normal">
              Russell Gillespie
            </h3>
            <div class="msg-conversation-card__mute-icon-holder
                msg-conversation-card__mute-icon-holder--inbox-shortcuts">
<!---->            </div>
              <time class="msg-overlay-list-bubble-item__time-stamp t-12
                  msg-overlay-list-bubble-item__time-stamp--inbox-shortcuts
                  t-normal t-black--light">
                May 15
              </time>
              <div class="msg-overlay-list-bubble__inbox-shortcuts-container">
                <div class="msg-overlay-list-bubble__inbox-shortcuts">
                  

<div id="ember157" class="artdeco-dropdown msg-thread-actions__dropdown artdeco-dropdown--placement-bottom artdeco-dropdown--justification-right ember-view">
  <button aria-expanded="false" id="ember158" class="msg-thread-actions__control artdeco-button artdeco-button--circle artdeco-button--1 artdeco-button--muted artdeco-button--tertiary artdeco-dropdown__trigger artdeco-dropdown__trigger--placement-bottom ember-view" type="button" tabindex="0">
    <li-icon aria-hidden="true" type="ellipsis-horizontal-icon" class="artdeco-button__icon" size="small" color="true"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" data-supported-dps="16x16" fill="currentColor" class="mercado-match" width="16" height="16" focusable="false">
  <path d="M3 9.5A1.5 1.5 0 114.5 8 1.5 1.5 0 013 9.5zM11.5 8A1.5 1.5 0 1013 6.5 1.5 1.5 0 0011.5 8zm-5 0A1.5 1.5 0 108 6.5 1.5 1.5 0 006.5 8z"></path>
</svg></li-icon>
    <span class="visually-hidden">
      Open the options list in your conversation with Russell Gillespie and Harith Al-Safi
    </span>
  
<!----></button>
  <div class="msg-thread-actions__dropdown-container">
    <div tabindex="-1" aria-hidden="true" id="ember159" class="msg-thread-actions__dropdown-options--inbox-shortcuts artdeco-dropdown__content artdeco-dropdown--is-dropdown-element artdeco-dropdown__content--has-arrow artdeco-dropdown__content--arrow-right artdeco-dropdown__content--justification-right artdeco-dropdown__content--placement-bottom ember-view"><!----></div>
  </div>
</div>

<!---->

<div>
<!----></div>

<!---->
                </div>
              </div>
          </div>

          <div class="msg-conversation-card__row justify-space-between">
            <div class="msg-overlay-list-bubble__message-snippet-container--narrow-two-line">
<!---->              <p class="msg-overlay-list-bubble__message-snippet--v2
                  
                  m0 t-12
                  t-black--light">
<!----><!---->                You: Thank you Russell that wouldn’t have been possible without your input 🙏🏻
              </p>
<!---->            </div>
            <div class="display-flex">
              <div class="msg-conversation-card__conversation-status msg-conversation-card__star-icon
                  ">
<!---->              </div>
<!---->            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
        <div class="msg-conversation-listitem__link msg-overlay-list-bubble__convo-item" tabindex="0" role="button" id="overlay-conversation-card-ember160" data-feedback-redacted="">
  <div class="msg-overlay-list-bubble__convo-card-container">
    <div class="msg-conversation-card msg-overlay-list-bubble__convo-card display-flex">
      <div class="msg-selectable-entity
    
    msg-selectable-entity--3">
      <div class="msg-facepile-grid--no-facepile msg-facepile-grid
    msg-facepile-grid--3 msg-selectable-entity__entity">
<!---->      <img src="https://media.licdn.com/dms/image/D4E03AQHIwwtL-uWrJA/profile-displayphoto-shrink_100_100/0/1667560391978?e=1691625600&amp;v=beta&amp;t=V-I4xJ1YCLTU4dQbgW01SGcToSi_ACsq0KKDqWS-gTo" loading="lazy" alt="Thomas Nascimento" id="ember232" class="evi-image lazy-image msg-facepile-grid__img msg-facepile-grid__img--person ember-view">
</div>
      <div class="msg-selectable-entity__checkbox-container">
    <input id="checkbox-msg-selectable-entity__checkbox-ember161" class="ember-checkbox ember-view msg-selectable-entity__input simple-form" type="checkbox">
    <label class="msg-selectable-entity__checkbox-label ml2" aria-label="Select conversation" for="checkbox-msg-selectable-entity__checkbox-ember161">
    </label>

    <div class="msg-selectable-entity__checkbox-circle-container">
      <div class="msg-selectable-entity__checkbox-circle">
      </div>
    </div>
  </div>
</div>

      <div class="overflow-hidden pl2
          msg-overlay-list-bubble__convo-card-content">
        <div class="msg-overlay-list-bubble__convo-card-content-wrapper fl">
          <div class="msg-conversation-card__row align-items-center display-flex">
            <h3 class="msg-conversation-listitem__participant-names msg-conversation-card__participant-names truncate t-14 t-black
                t-normal">
              Thomas Nascimento
            </h3>
            <div class="msg-conversation-card__mute-icon-holder
                msg-conversation-card__mute-icon-holder--inbox-shortcuts">
<!---->            </div>
              <time class="msg-overlay-list-bubble-item__time-stamp t-12
                  msg-overlay-list-bubble-item__time-stamp--inbox-shortcuts
                  t-normal t-black--light">
                May 4
              </time>
              <div class="msg-overlay-list-bubble__inbox-shortcuts-container">
                <div class="msg-overlay-list-bubble__inbox-shortcuts">
                  

<div id="ember163" class="artdeco-dropdown msg-thread-actions__dropdown artdeco-dropdown--placement-bottom artdeco-dropdown--justification-right ember-view">
  <button aria-expanded="false" id="ember164" class="msg-thread-actions__control artdeco-button artdeco-button--circle artdeco-button--1 artdeco-button--muted artdeco-button--tertiary artdeco-dropdown__trigger artdeco-dropdown__trigger--placement-bottom ember-view" type="button" tabindex="0">
    <li-icon aria-hidden="true" type="ellipsis-horizontal-icon" class="artdeco-button__icon" size="small" color="true"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" data-supported-dps="16x16" fill="currentColor" class="mercado-match" width="16" height="16" focusable="false">
  <path d="M3 9.5A1.5 1.5 0 114.5 8 1.5 1.5 0 013 9.5zM11.5 8A1.5 1.5 0 1013 6.5 1.5 1.5 0 0011.5 8zm-5 0A1.5 1.5 0 108 6.5 1.5 1.5 0 006.5 8z"></path>
</svg></li-icon>
    <span class="visually-hidden">
      Open the options list in your conversation with Thomas Nascimento and Harith Al-Safi
    </span>
  
<!----></button>
  <div class="msg-thread-actions__dropdown-container">
    <div tabindex="-1" aria-hidden="true" id="ember165" class="msg-thread-actions__dropdown-options--inbox-shortcuts artdeco-dropdown__content artdeco-dropdown--is-dropdown-element artdeco-dropdown__content--has-arrow artdeco-dropdown__content--arrow-right artdeco-dropdown__content--justification-right artdeco-dropdown__content--placement-bottom ember-view"><!----></div>
  </div>
</div>

<!---->

<div>
<!----></div>

<!---->
                </div>
              </div>
          </div>

          <div class="msg-conversation-card__row justify-space-between">
            <div class="msg-overlay-list-bubble__message-snippet-container--narrow-two-line">
<!---->              <p class="msg-overlay-list-bubble__message-snippet--v2
                  
                  m0 t-12
                  t-black--light">
<!----><!---->                Amazon Web Services (AWS) Internship 2023 in Cambridge, UK
              </p>
<!---->            </div>
            <div class="display-flex">
              <div class="msg-conversation-card__conversation-status msg-conversation-card__star-icon
                  ">
<!---->              </div>
<!---->            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
        <div class="msg-conversation-listitem__link msg-overlay-list-bubble__convo-item" tabindex="0" role="button" id="overlay-conversation-card-ember166" data-feedback-redacted="">
  <div class="msg-overlay-list-bubble__convo-card-container">
    <div class="msg-conversation-card msg-overlay-list-bubble__convo-card display-flex">
      <div class="msg-selectable-entity
    
    msg-selectable-entity--3">
      <div class="presence-entity presence-entity--size-3 msg-selectable-entity__entity">
  <img src="https://media.licdn.com/dms/image/C5603AQFudm_rarWfrA/profile-displayphoto-shrink_100_100/0/1578869139586?e=1691625600&amp;v=beta&amp;t=np4z9CH-6zPbV1TaosaSX4BKcUBBwZJotT6_4ooLXu0" loading="lazy" alt="Jacky Lam" id="ember168" class="presence-entity__image EntityPhoto-circle-3  evi-image lazy-image ember-view">

    
<div class="presence-entity__indicator presence-entity__indicator--size-3
         presence-indicator
    hidden
    presence-indicator--size-3">
  <span class="visually-hidden">
      Status is offline
      </span>
</div>
</div>
  <div class="msg-selectable-entity__checkbox-container">
    <input id="checkbox-msg-selectable-entity__checkbox-ember167" class="ember-checkbox ember-view msg-selectable-entity__input simple-form" type="checkbox">
    <label class="msg-selectable-entity__checkbox-label ml2" aria-label="Select conversation" for="checkbox-msg-selectable-entity__checkbox-ember167">
    </label>

    <div class="msg-selectable-entity__checkbox-circle-container">
      <div class="msg-selectable-entity__checkbox-circle">
      </div>
    </div>
  </div>
</div>

      <div class="overflow-hidden pl2
          msg-overlay-list-bubble__convo-card-content">
        <div class="msg-overlay-list-bubble__convo-card-content-wrapper fl">
          <div class="msg-conversation-card__row align-items-center display-flex">
            <h3 class="msg-conversation-listitem__participant-names msg-conversation-card__participant-names truncate t-14 t-black
                t-normal">
              Jacky Lam
            </h3>
            <div class="msg-conversation-card__mute-icon-holder
                msg-conversation-card__mute-icon-holder--inbox-shortcuts">
<!---->            </div>
              <time class="msg-overlay-list-bubble-item__time-stamp t-12
                  msg-overlay-list-bubble-item__time-stamp--inbox-shortcuts
                  t-normal t-black--light">
                Apr 30
              </time>
              <div class="msg-overlay-list-bubble__inbox-shortcuts-container">
                <div class="msg-overlay-list-bubble__inbox-shortcuts">
                  

<div id="ember169" class="artdeco-dropdown msg-thread-actions__dropdown artdeco-dropdown--placement-bottom artdeco-dropdown--justification-right ember-view">
  <button aria-expanded="false" id="ember170" class="msg-thread-actions__control artdeco-button artdeco-button--circle artdeco-button--1 artdeco-button--muted artdeco-button--tertiary artdeco-dropdown__trigger artdeco-dropdown__trigger--placement-bottom ember-view" type="button" tabindex="0">
    <li-icon aria-hidden="true" type="ellipsis-horizontal-icon" class="artdeco-button__icon" size="small" color="true"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" data-supported-dps="16x16" fill="currentColor" class="mercado-match" width="16" height="16" focusable="false">
  <path d="M3 9.5A1.5 1.5 0 114.5 8 1.5 1.5 0 013 9.5zM11.5 8A1.5 1.5 0 1013 6.5 1.5 1.5 0 0011.5 8zm-5 0A1.5 1.5 0 108 6.5 1.5 1.5 0 006.5 8z"></path>
</svg></li-icon>
    <span class="visually-hidden">
      Open the options list in your conversation with Jacky Lam and Harith Al-Safi
    </span>
  
<!----></button>
  <div class="msg-thread-actions__dropdown-container">
    <div tabindex="-1" aria-hidden="true" id="ember171" class="msg-thread-actions__dropdown-options--inbox-shortcuts artdeco-dropdown__content artdeco-dropdown--is-dropdown-element artdeco-dropdown__content--has-arrow artdeco-dropdown__content--arrow-right artdeco-dropdown__content--justification-right artdeco-dropdown__content--placement-bottom ember-view"><!----></div>
  </div>
</div>

<!---->

<div>
<!----></div>

<!---->
                </div>
              </div>
          </div>

          <div class="msg-conversation-card__row justify-space-between">
            <div class="msg-overlay-list-bubble__message-snippet-container--narrow-two-line">
<!---->              <p class="msg-overlay-list-bubble__message-snippet--v2
                  
                  m0 t-12
                  t-black--light">
<!----><!---->                You: I thought ninjatrader is only a platform rather than broker
              </p>
<!---->            </div>
            <div class="display-flex">
              <div class="msg-conversation-card__conversation-status msg-conversation-card__star-icon
                  ">
<!---->              </div>
<!---->            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
        <div class="msg-conversation-listitem__link msg-overlay-list-bubble__convo-item" tabindex="0" role="button" id="overlay-conversation-card-ember172" data-feedback-redacted="">
  <div class="msg-overlay-list-bubble__convo-card-container">
    <div class="msg-conversation-card msg-overlay-list-bubble__convo-card display-flex">
      <div class="msg-selectable-entity
    
    msg-selectable-entity--3">
      <div class="msg-facepile-grid--no-facepile msg-facepile-grid
    msg-facepile-grid--3 msg-selectable-entity__entity">
<!---->      <img src="https://media.licdn.com/dms/image/C5603AQG8FeTrRYS2GQ/profile-displayphoto-shrink_100_100/0/1654771039138?e=1691625600&amp;v=beta&amp;t=iaMxP2sB05N7AH5AqMUvmREJhZSTFlOwwOVQT-sBjGY" loading="lazy" alt="Paola Hernandez" id="ember233" class="evi-image lazy-image msg-facepile-grid__img msg-facepile-grid__img--person ember-view">
</div>
      <div class="msg-selectable-entity__checkbox-container">
    <input id="checkbox-msg-selectable-entity__checkbox-ember173" class="ember-checkbox ember-view msg-selectable-entity__input simple-form" type="checkbox">
    <label class="msg-selectable-entity__checkbox-label ml2" aria-label="Select conversation" for="checkbox-msg-selectable-entity__checkbox-ember173">
    </label>

    <div class="msg-selectable-entity__checkbox-circle-container">
      <div class="msg-selectable-entity__checkbox-circle">
      </div>
    </div>
  </div>
</div>

      <div class="overflow-hidden pl2
          msg-overlay-list-bubble__convo-card-content">
        <div class="msg-overlay-list-bubble__convo-card-content-wrapper fl">
          <div class="msg-conversation-card__row align-items-center display-flex">
            <h3 class="msg-conversation-listitem__participant-names msg-conversation-card__participant-names truncate t-14 t-black
                t-normal">
              Paola Hernandez
            </h3>
            <div class="msg-conversation-card__mute-icon-holder
                msg-conversation-card__mute-icon-holder--inbox-shortcuts">
<!---->            </div>
              <time class="msg-overlay-list-bubble-item__time-stamp t-12
                  msg-overlay-list-bubble-item__time-stamp--inbox-shortcuts
                  t-normal t-black--light">
                Apr 26
              </time>
              <div class="msg-overlay-list-bubble__inbox-shortcuts-container">
                <div class="msg-overlay-list-bubble__inbox-shortcuts">
                  

<div id="ember175" class="artdeco-dropdown msg-thread-actions__dropdown artdeco-dropdown--placement-bottom artdeco-dropdown--justification-right ember-view">
  <button aria-expanded="false" id="ember176" class="msg-thread-actions__control artdeco-button artdeco-button--circle artdeco-button--1 artdeco-button--muted artdeco-button--tertiary artdeco-dropdown__trigger artdeco-dropdown__trigger--placement-bottom ember-view" type="button" tabindex="0">
    <li-icon aria-hidden="true" type="ellipsis-horizontal-icon" class="artdeco-button__icon" size="small" color="true"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" data-supported-dps="16x16" fill="currentColor" class="mercado-match" width="16" height="16" focusable="false">
  <path d="M3 9.5A1.5 1.5 0 114.5 8 1.5 1.5 0 013 9.5zM11.5 8A1.5 1.5 0 1013 6.5 1.5 1.5 0 0011.5 8zm-5 0A1.5 1.5 0 108 6.5 1.5 1.5 0 006.5 8z"></path>
</svg></li-icon>
    <span class="visually-hidden">
      Open the options list in your conversation with Harith Al-Safi and Paola Hernandez
    </span>
  
<!----></button>
  <div class="msg-thread-actions__dropdown-container">
    <div tabindex="-1" aria-hidden="true" id="ember177" class="msg-thread-actions__dropdown-options--inbox-shortcuts artdeco-dropdown__content artdeco-dropdown--is-dropdown-element artdeco-dropdown__content--has-arrow artdeco-dropdown__content--arrow-right artdeco-dropdown__content--justification-right artdeco-dropdown__content--placement-bottom ember-view"><!----></div>
  </div>
</div>

<!---->

<div>
<!----></div>

<!---->
                </div>
              </div>
          </div>

          <div class="msg-conversation-card__row justify-space-between">
            <div class="msg-overlay-list-bubble__message-snippet-container--narrow-two-line">
<!---->              <p class="msg-overlay-list-bubble__message-snippet--v2
                  
                  m0 t-12
                  t-black--light">
<!----><!---->                Keeping your options open?
              </p>
<!---->            </div>
            <div class="display-flex">
              <div class="msg-conversation-card__conversation-status msg-conversation-card__star-icon
                  ">
<!---->              </div>
<!---->            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
        <div class="msg-conversation-listitem__link msg-overlay-list-bubble__convo-item" tabindex="0" role="button" id="overlay-conversation-card-ember178" data-feedback-redacted="">
  <div class="msg-overlay-list-bubble__convo-card-container">
    <div class="msg-conversation-card msg-overlay-list-bubble__convo-card display-flex">
      <div class="msg-selectable-entity
    
    msg-selectable-entity--3">
      <div class="msg-facepile-grid--no-facepile msg-facepile-grid
    msg-facepile-grid--3 msg-selectable-entity__entity">
<!---->      <img src="https://media.licdn.com/dms/image/C4D03AQH304aZ_RM4Wg/profile-displayphoto-shrink_100_100/0/1630584805409?e=1691625600&amp;v=beta&amp;t=03HUduHLBx63GKKfF1cuHOV_QOsf10Zb2dSADsJqCtw" loading="lazy" alt="Ben Fox" id="ember234" class="evi-image lazy-image msg-facepile-grid__img msg-facepile-grid__img--person ember-view">
</div>
      <div class="msg-selectable-entity__checkbox-container">
    <input id="checkbox-msg-selectable-entity__checkbox-ember179" class="ember-checkbox ember-view msg-selectable-entity__input simple-form" type="checkbox">
    <label class="msg-selectable-entity__checkbox-label ml2" aria-label="Select conversation" for="checkbox-msg-selectable-entity__checkbox-ember179">
    </label>

    <div class="msg-selectable-entity__checkbox-circle-container">
      <div class="msg-selectable-entity__checkbox-circle">
      </div>
    </div>
  </div>
</div>

      <div class="overflow-hidden pl2
          msg-overlay-list-bubble__convo-card-content">
        <div class="msg-overlay-list-bubble__convo-card-content-wrapper fl">
          <div class="msg-conversation-card__row align-items-center display-flex">
            <h3 class="msg-conversation-listitem__participant-names msg-conversation-card__participant-names truncate t-14 t-black
                t-normal">
              Ben Fox
            </h3>
            <div class="msg-conversation-card__mute-icon-holder
                msg-conversation-card__mute-icon-holder--inbox-shortcuts">
<!---->            </div>
              <time class="msg-overlay-list-bubble-item__time-stamp t-12
                  msg-overlay-list-bubble-item__time-stamp--inbox-shortcuts
                  t-normal t-black--light">
                Apr 24
              </time>
              <div class="msg-overlay-list-bubble__inbox-shortcuts-container">
                <div class="msg-overlay-list-bubble__inbox-shortcuts">
                  

<div id="ember181" class="artdeco-dropdown msg-thread-actions__dropdown artdeco-dropdown--placement-bottom artdeco-dropdown--justification-right ember-view">
  <button aria-expanded="false" id="ember182" class="msg-thread-actions__control artdeco-button artdeco-button--circle artdeco-button--1 artdeco-button--muted artdeco-button--tertiary artdeco-dropdown__trigger artdeco-dropdown__trigger--placement-bottom ember-view" type="button" tabindex="0">
    <li-icon aria-hidden="true" type="ellipsis-horizontal-icon" class="artdeco-button__icon" size="small" color="true"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" data-supported-dps="16x16" fill="currentColor" class="mercado-match" width="16" height="16" focusable="false">
  <path d="M3 9.5A1.5 1.5 0 114.5 8 1.5 1.5 0 013 9.5zM11.5 8A1.5 1.5 0 1013 6.5 1.5 1.5 0 0011.5 8zm-5 0A1.5 1.5 0 108 6.5 1.5 1.5 0 006.5 8z"></path>
</svg></li-icon>
    <span class="visually-hidden">
      Open the options list in your conversation with Ben Fox and Harith Al-Safi
    </span>
  
<!----></button>
  <div class="msg-thread-actions__dropdown-container">
    <div tabindex="-1" aria-hidden="true" id="ember183" class="msg-thread-actions__dropdown-options--inbox-shortcuts artdeco-dropdown__content artdeco-dropdown--is-dropdown-element artdeco-dropdown__content--has-arrow artdeco-dropdown__content--arrow-right artdeco-dropdown__content--justification-right artdeco-dropdown__content--placement-bottom ember-view"><!----></div>
  </div>
</div>

<!---->

<div>
<!----></div>

<!---->
                </div>
              </div>
          </div>

          <div class="msg-conversation-card__row justify-space-between">
            <div class="msg-overlay-list-bubble__message-snippet-container--narrow-two-line">
<!---->              <p class="msg-overlay-list-bubble__message-snippet--v2
                  
                  m0 t-12
                  t-black--light">
<!----><!---->                Want to push the boundaries of Java Development?
              </p>
<!---->            </div>
            <div class="display-flex">
              <div class="msg-conversation-card__conversation-status msg-conversation-card__star-icon
                  ">
<!---->              </div>
<!---->            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
        <div class="msg-conversation-listitem__link msg-overlay-list-bubble__convo-item" tabindex="0" role="button" id="overlay-conversation-card-ember184" data-feedback-redacted="">
  <div class="msg-overlay-list-bubble__convo-card-container">
    <div class="msg-conversation-card msg-overlay-list-bubble__convo-card display-flex">
      <div class="msg-selectable-entity
    
    msg-selectable-entity--3">
      <div class="msg-facepile-grid--no-facepile msg-facepile-grid
    msg-facepile-grid--3 msg-selectable-entity__entity">
<!---->      <img src="https://media.licdn.com/dms/image/D4E03AQFTew-fcXra_w/profile-displayphoto-shrink_100_100/0/1681392512150?e=1691625600&amp;v=beta&amp;t=O7byNVK-RZCNVBcjU1GS9Kfh9Uikkd4dK24jFhFP1zM" loading="lazy" alt="Gurpal Bhogal" id="ember235" class="evi-image lazy-image msg-facepile-grid__img msg-facepile-grid__img--person ember-view">
</div>
      <div class="msg-selectable-entity__checkbox-container">
    <input id="checkbox-msg-selectable-entity__checkbox-ember185" class="ember-checkbox ember-view msg-selectable-entity__input simple-form" type="checkbox">
    <label class="msg-selectable-entity__checkbox-label ml2" aria-label="Select conversation" for="checkbox-msg-selectable-entity__checkbox-ember185">
    </label>

    <div class="msg-selectable-entity__checkbox-circle-container">
      <div class="msg-selectable-entity__checkbox-circle">
      </div>
    </div>
  </div>
</div>

      <div class="overflow-hidden pl2
          msg-overlay-list-bubble__convo-card-content">
        <div class="msg-overlay-list-bubble__convo-card-content-wrapper fl">
          <div class="msg-conversation-card__row align-items-center display-flex">
            <h3 class="msg-conversation-listitem__participant-names msg-conversation-card__participant-names truncate t-14 t-black
                t-normal">
              Gurpal Bhogal
            </h3>
            <div class="msg-conversation-card__mute-icon-holder
                msg-conversation-card__mute-icon-holder--inbox-shortcuts">
<!---->            </div>
              <time class="msg-overlay-list-bubble-item__time-stamp t-12
                  msg-overlay-list-bubble-item__time-stamp--inbox-shortcuts
                  t-normal t-black--light">
                Apr 19
              </time>
              <div class="msg-overlay-list-bubble__inbox-shortcuts-container">
                <div class="msg-overlay-list-bubble__inbox-shortcuts">
                  

<div id="ember187" class="artdeco-dropdown msg-thread-actions__dropdown artdeco-dropdown--placement-bottom artdeco-dropdown--justification-right ember-view">
  <button aria-expanded="false" id="ember188" class="msg-thread-actions__control artdeco-button artdeco-button--circle artdeco-button--1 artdeco-button--muted artdeco-button--tertiary artdeco-dropdown__trigger artdeco-dropdown__trigger--placement-bottom ember-view" type="button" tabindex="0">
    <li-icon aria-hidden="true" type="ellipsis-horizontal-icon" class="artdeco-button__icon" size="small" color="true"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" data-supported-dps="16x16" fill="currentColor" class="mercado-match" width="16" height="16" focusable="false">
  <path d="M3 9.5A1.5 1.5 0 114.5 8 1.5 1.5 0 013 9.5zM11.5 8A1.5 1.5 0 1013 6.5 1.5 1.5 0 0011.5 8zm-5 0A1.5 1.5 0 108 6.5 1.5 1.5 0 006.5 8z"></path>
</svg></li-icon>
    <span class="visually-hidden">
      Open the options list in your conversation with Gurpal Bhogal
    </span>
  
<!----></button>
  <div class="msg-thread-actions__dropdown-container">
    <div tabindex="-1" aria-hidden="true" id="ember189" class="msg-thread-actions__dropdown-options--inbox-shortcuts artdeco-dropdown__content artdeco-dropdown--is-dropdown-element artdeco-dropdown__content--has-arrow artdeco-dropdown__content--arrow-right artdeco-dropdown__content--justification-right artdeco-dropdown__content--placement-bottom ember-view"><!----></div>
  </div>
</div>

<!---->

<div>
<!----></div>

<!---->
                </div>
              </div>
          </div>

          <div class="msg-conversation-card__row justify-space-between">
            <div class="msg-overlay-list-bubble__message-snippet-container--narrow-two-line">
<!---->              <p class="msg-overlay-list-bubble__message-snippet--v2
                  
                  m0 t-12
                  t-black--light">
<!---->                  <span class="msg-conversation-card__pill t-14
                       t-black 
                      t-bold pr1">
                    Sponsored
                  </span>
                Become AI Job ready
              </p>
<!---->            </div>
            <div class="display-flex">
              <div class="msg-conversation-card__conversation-status msg-conversation-card__star-icon
                  ">
<!---->              </div>
<!---->            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
        <div class="msg-conversation-listitem__link msg-overlay-list-bubble__convo-item" tabindex="0" role="button" id="overlay-conversation-card-ember190" data-feedback-redacted="">
  <div class="msg-overlay-list-bubble__convo-card-container">
    <div class="msg-conversation-card msg-overlay-list-bubble__convo-card display-flex">
      <div class="msg-selectable-entity
    
    msg-selectable-entity--3">
      <div class="msg-facepile-grid--no-facepile msg-facepile-grid
    msg-facepile-grid--3 msg-selectable-entity__entity">
<!---->      <img src="https://media.licdn.com/dms/image/C4D03AQF942SSkruymg/profile-displayphoto-shrink_100_100/0/1662135165019?e=1691625600&amp;v=beta&amp;t=OyBZ8RUaQt8EFJdL0z4_GPdc2q7vEsCH7B67zvCKvqU" loading="lazy" alt="Adam Smith" id="ember236" class="evi-image lazy-image msg-facepile-grid__img msg-facepile-grid__img--person ember-view">
</div>
      <div class="msg-selectable-entity__checkbox-container">
    <input id="checkbox-msg-selectable-entity__checkbox-ember191" class="ember-checkbox ember-view msg-selectable-entity__input simple-form" type="checkbox">
    <label class="msg-selectable-entity__checkbox-label ml2" aria-label="Select conversation" for="checkbox-msg-selectable-entity__checkbox-ember191">
    </label>

    <div class="msg-selectable-entity__checkbox-circle-container">
      <div class="msg-selectable-entity__checkbox-circle">
      </div>
    </div>
  </div>
</div>

      <div class="overflow-hidden pl2
          msg-overlay-list-bubble__convo-card-content">
        <div class="msg-overlay-list-bubble__convo-card-content-wrapper fl">
          <div class="msg-conversation-card__row align-items-center display-flex">
            <h3 class="msg-conversation-listitem__participant-names msg-conversation-card__participant-names truncate t-14 t-black
                t-normal">
              Adam Smith
            </h3>
            <div class="msg-conversation-card__mute-icon-holder
                msg-conversation-card__mute-icon-holder--inbox-shortcuts">
<!---->            </div>
              <time class="msg-overlay-list-bubble-item__time-stamp t-12
                  msg-overlay-list-bubble-item__time-stamp--inbox-shortcuts
                  t-normal t-black--light">
                Apr 17
              </time>
              <div class="msg-overlay-list-bubble__inbox-shortcuts-container">
                <div class="msg-overlay-list-bubble__inbox-shortcuts">
                  

<div id="ember193" class="artdeco-dropdown msg-thread-actions__dropdown artdeco-dropdown--placement-bottom artdeco-dropdown--justification-right ember-view">
  <button aria-expanded="false" id="ember194" class="msg-thread-actions__control artdeco-button artdeco-button--circle artdeco-button--1 artdeco-button--muted artdeco-button--tertiary artdeco-dropdown__trigger artdeco-dropdown__trigger--placement-bottom ember-view" type="button" tabindex="0">
    <li-icon aria-hidden="true" type="ellipsis-horizontal-icon" class="artdeco-button__icon" size="small" color="true"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" data-supported-dps="16x16" fill="currentColor" class="mercado-match" width="16" height="16" focusable="false">
  <path d="M3 9.5A1.5 1.5 0 114.5 8 1.5 1.5 0 013 9.5zM11.5 8A1.5 1.5 0 1013 6.5 1.5 1.5 0 0011.5 8zm-5 0A1.5 1.5 0 108 6.5 1.5 1.5 0 006.5 8z"></path>
</svg></li-icon>
    <span class="visually-hidden">
      Open the options list in your conversation with Adam Smith and Harith Al-Safi
    </span>
  
<!----></button>
  <div class="msg-thread-actions__dropdown-container">
    <div tabindex="-1" aria-hidden="true" id="ember195" class="msg-thread-actions__dropdown-options--inbox-shortcuts artdeco-dropdown__content artdeco-dropdown--is-dropdown-element artdeco-dropdown__content--has-arrow artdeco-dropdown__content--arrow-right artdeco-dropdown__content--justification-right artdeco-dropdown__content--placement-bottom ember-view"><!----></div>
  </div>
</div>

<!---->

<div>
<!----></div>

<!---->
                </div>
              </div>
          </div>

          <div class="msg-conversation-card__row justify-space-between">
            <div class="msg-overlay-list-bubble__message-snippet-container--narrow-two-line">
<!---->              <p class="msg-overlay-list-bubble__message-snippet--v2
                  
                  m0 t-12
                  t-black--light">
<!----><!---->                Software Developer- JN Bentley
              </p>
<!---->            </div>
            <div class="display-flex">
              <div class="msg-conversation-card__conversation-status msg-conversation-card__star-icon
                  ">
<!---->              </div>
<!---->            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
        <div class="msg-conversation-listitem__link msg-overlay-list-bubble__convo-item" tabindex="0" role="button" id="overlay-conversation-card-ember196" data-feedback-redacted="">
  <div class="msg-overlay-list-bubble__convo-card-container">
    <div class="msg-conversation-card msg-overlay-list-bubble__convo-card display-flex">
      <div class="msg-selectable-entity
    
    msg-selectable-entity--3">
      <div class="presence-entity presence-entity--size-3 msg-selectable-entity__entity">
  <img src="https://media.licdn.com/dms/image/C5603AQFzpRNlugdYVA/profile-displayphoto-shrink_100_100/0/1579011134031?e=1691625600&amp;v=beta&amp;t=47u21Y99m--mCPT-gHrTlY3nccDMK4wkPpYZBM2ipSI" loading="lazy" alt="Caroline Dhillon" id="ember198" class="presence-entity__image EntityPhoto-circle-3  evi-image lazy-image ember-view">

    
<div class="presence-entity__indicator presence-entity__indicator--size-3
         presence-indicator
    presence-indicator--is-reachable
    presence-indicator--size-3">
  <span class="visually-hidden">
      Status is reachable
  </span>
</div>
</div>
  <div class="msg-selectable-entity__checkbox-container">
    <input id="checkbox-msg-selectable-entity__checkbox-ember197" class="ember-checkbox ember-view msg-selectable-entity__input simple-form" type="checkbox">
    <label class="msg-selectable-entity__checkbox-label ml2" aria-label="Select conversation" for="checkbox-msg-selectable-entity__checkbox-ember197">
    </label>

    <div class="msg-selectable-entity__checkbox-circle-container">
      <div class="msg-selectable-entity__checkbox-circle">
      </div>
    </div>
  </div>
</div>

      <div class="overflow-hidden pl2
          msg-overlay-list-bubble__convo-card-content">
        <div class="msg-overlay-list-bubble__convo-card-content-wrapper fl">
          <div class="msg-conversation-card__row align-items-center display-flex">
            <h3 class="msg-conversation-listitem__participant-names msg-conversation-card__participant-names truncate t-14 t-black
                t-normal">
              Caroline Dhillon
            </h3>
            <div class="msg-conversation-card__mute-icon-holder
                msg-conversation-card__mute-icon-holder--inbox-shortcuts">
<!---->            </div>
              <time class="msg-overlay-list-bubble-item__time-stamp t-12
                  msg-overlay-list-bubble-item__time-stamp--inbox-shortcuts
                  t-normal t-black--light">
                Apr 9
              </time>
              <div class="msg-overlay-list-bubble__inbox-shortcuts-container">
                <div class="msg-overlay-list-bubble__inbox-shortcuts">
                  

<div id="ember199" class="artdeco-dropdown msg-thread-actions__dropdown artdeco-dropdown--placement-bottom artdeco-dropdown--justification-right ember-view">
  <button aria-expanded="false" id="ember200" class="msg-thread-actions__control artdeco-button artdeco-button--circle artdeco-button--1 artdeco-button--muted artdeco-button--tertiary artdeco-dropdown__trigger artdeco-dropdown__trigger--placement-bottom ember-view" type="button" tabindex="0">
    <li-icon aria-hidden="true" type="ellipsis-horizontal-icon" class="artdeco-button__icon" size="small" color="true"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" data-supported-dps="16x16" fill="currentColor" class="mercado-match" width="16" height="16" focusable="false">
  <path d="M3 9.5A1.5 1.5 0 114.5 8 1.5 1.5 0 013 9.5zM11.5 8A1.5 1.5 0 1013 6.5 1.5 1.5 0 0011.5 8zm-5 0A1.5 1.5 0 108 6.5 1.5 1.5 0 006.5 8z"></path>
</svg></li-icon>
    <span class="visually-hidden">
      Open the options list in your conversation with Caroline Dhillon and Harith Al-Safi
    </span>
  
<!----></button>
  <div class="msg-thread-actions__dropdown-container">
    <div tabindex="-1" aria-hidden="true" id="ember201" class="msg-thread-actions__dropdown-options--inbox-shortcuts artdeco-dropdown__content artdeco-dropdown--is-dropdown-element artdeco-dropdown__content--has-arrow artdeco-dropdown__content--arrow-right artdeco-dropdown__content--justification-right artdeco-dropdown__content--placement-bottom ember-view"><!----></div>
  </div>
</div>

<!---->

<div>
<!----></div>

<!---->
                </div>
              </div>
          </div>

          <div class="msg-conversation-card__row justify-space-between">
            <div class="msg-overlay-list-bubble__message-snippet-container--narrow-two-line">
<!---->              <p class="msg-overlay-list-bubble__message-snippet--v2
                  
                  m0 t-12
                  t-black--light">
<!----><!---->                You: Hey Caroline
I hope you are doing well

I just saw that you work in HR, for splunk and I noticed there is an open position for a summer internship in London for software engineering. I was wondering if there are any tips you could give me to help secure this role.

Thanks alot 
              </p>
<!---->            </div>
            <div class="display-flex">
              <div class="msg-conversation-card__conversation-status msg-conversation-card__star-icon
                  ">
<!---->              </div>
<!---->            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
        <div class="msg-conversation-listitem__link msg-overlay-list-bubble__convo-item" tabindex="0" role="button" id="overlay-conversation-card-ember202" data-feedback-redacted="">
  <div class="msg-overlay-list-bubble__convo-card-container">
    <div class="msg-conversation-card msg-overlay-list-bubble__convo-card display-flex">
      <div class="msg-selectable-entity
    
    msg-selectable-entity--3">
      <div class="msg-facepile-grid--no-facepile msg-facepile-grid
    msg-facepile-grid--3 msg-selectable-entity__entity">
<!---->      <img src="https://media.licdn.com/dms/image/C4E03AQEHaZqFgf97yg/profile-displayphoto-shrink_100_100/0/1606490191291?e=1691625600&amp;v=beta&amp;t=A4oeBk8iErUH2uZ8x7gP7zIdpqzUVeW6L-lWpNBZt5U" loading="lazy" alt="Thea Maloney Assoc. CIPD" id="ember237" class="evi-image lazy-image msg-facepile-grid__img msg-facepile-grid__img--person ember-view">
</div>
      <div class="msg-selectable-entity__checkbox-container">
    <input id="checkbox-msg-selectable-entity__checkbox-ember203" class="ember-checkbox ember-view msg-selectable-entity__input simple-form" type="checkbox">
    <label class="msg-selectable-entity__checkbox-label ml2" aria-label="Select conversation" for="checkbox-msg-selectable-entity__checkbox-ember203">
    </label>

    <div class="msg-selectable-entity__checkbox-circle-container">
      <div class="msg-selectable-entity__checkbox-circle">
      </div>
    </div>
  </div>
</div>

      <div class="overflow-hidden pl2
          msg-overlay-list-bubble__convo-card-content">
        <div class="msg-overlay-list-bubble__convo-card-content-wrapper fl">
          <div class="msg-conversation-card__row align-items-center display-flex">
            <h3 class="msg-conversation-listitem__participant-names msg-conversation-card__participant-names truncate t-14 t-black
                t-normal">
              Thea Maloney Assoc. CIPD
            </h3>
            <div class="msg-conversation-card__mute-icon-holder
                msg-conversation-card__mute-icon-holder--inbox-shortcuts">
<!---->            </div>
              <time class="msg-overlay-list-bubble-item__time-stamp t-12
                  msg-overlay-list-bubble-item__time-stamp--inbox-shortcuts
                  t-normal t-black--light">
                Apr 9
              </time>
              <div class="msg-overlay-list-bubble__inbox-shortcuts-container">
                <div class="msg-overlay-list-bubble__inbox-shortcuts">
                  

<div id="ember205" class="artdeco-dropdown msg-thread-actions__dropdown artdeco-dropdown--placement-bottom artdeco-dropdown--justification-right ember-view">
  <button aria-expanded="false" id="ember206" class="msg-thread-actions__control artdeco-button artdeco-button--circle artdeco-button--1 artdeco-button--muted artdeco-button--tertiary artdeco-dropdown__trigger artdeco-dropdown__trigger--placement-bottom ember-view" type="button" tabindex="0">
    <li-icon aria-hidden="true" type="ellipsis-horizontal-icon" class="artdeco-button__icon" size="small" color="true"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" data-supported-dps="16x16" fill="currentColor" class="mercado-match" width="16" height="16" focusable="false">
  <path d="M3 9.5A1.5 1.5 0 114.5 8 1.5 1.5 0 013 9.5zM11.5 8A1.5 1.5 0 1013 6.5 1.5 1.5 0 0011.5 8zm-5 0A1.5 1.5 0 108 6.5 1.5 1.5 0 006.5 8z"></path>
</svg></li-icon>
    <span class="visually-hidden">
      Open the options list in your conversation with Thea Maloney Assoc. CIPD and Harith Al-Safi
    </span>
  
<!----></button>
  <div class="msg-thread-actions__dropdown-container">
    <div tabindex="-1" aria-hidden="true" id="ember207" class="msg-thread-actions__dropdown-options--inbox-shortcuts artdeco-dropdown__content artdeco-dropdown--is-dropdown-element artdeco-dropdown__content--has-arrow artdeco-dropdown__content--arrow-right artdeco-dropdown__content--justification-right artdeco-dropdown__content--placement-bottom ember-view"><!----></div>
  </div>
</div>

<!---->

<div>
<!----></div>

<!---->
                </div>
              </div>
          </div>

          <div class="msg-conversation-card__row justify-space-between">
            <div class="msg-overlay-list-bubble__message-snippet-container--narrow-two-line">
<!---->              <p class="msg-overlay-list-bubble__message-snippet--v2
                  
                  m0 t-12
                  t-black--light">
<!---->                  <span class="msg-conversation-card__pill t-14
                       t-black 
                      t-bold pr1">
                    InMail
                  </span>
                You: Dear Thea
I hope you are doing well
I just saw that you work in HR for Cboe, and they had a C++ internship. So I wanted to see if it’s available and if there are any tips you could give me to get that role.
Thank you!
              </p>
<!---->            </div>
            <div class="display-flex">
              <div class="msg-conversation-card__conversation-status msg-conversation-card__star-icon
                  ">
<!---->              </div>
<!---->            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
        <div class="msg-conversation-listitem__link msg-overlay-list-bubble__convo-item" tabindex="0" role="button" id="overlay-conversation-card-ember208" data-feedback-redacted="">
  <div class="msg-overlay-list-bubble__convo-card-container">
    <div class="msg-conversation-card msg-overlay-list-bubble__convo-card display-flex">
      <div class="msg-selectable-entity
    
    msg-selectable-entity--3">
      <div class="msg-facepile-grid--no-facepile msg-facepile-grid
    msg-facepile-grid--3 msg-selectable-entity__entity">
<!---->      <img src="https://media.licdn.com/dms/image/D4E03AQG8VN42uNJNkg/profile-displayphoto-shrink_100_100/0/1682525983244?e=1691625600&amp;v=beta&amp;t=sr6Wu8z0l8iH-XtvffQPCTWFHNsMRLYL3wcDNK05Ys0" loading="lazy" alt="Mark Stevenson" id="ember238" class="evi-image lazy-image msg-facepile-grid__img msg-facepile-grid__img--person ember-view">
</div>
      <div class="msg-selectable-entity__checkbox-container">
    <input id="checkbox-msg-selectable-entity__checkbox-ember209" class="ember-checkbox ember-view msg-selectable-entity__input simple-form" type="checkbox">
    <label class="msg-selectable-entity__checkbox-label ml2" aria-label="Select conversation" for="checkbox-msg-selectable-entity__checkbox-ember209">
    </label>

    <div class="msg-selectable-entity__checkbox-circle-container">
      <div class="msg-selectable-entity__checkbox-circle">
      </div>
    </div>
  </div>
</div>

      <div class="overflow-hidden pl2
          msg-overlay-list-bubble__convo-card-content">
        <div class="msg-overlay-list-bubble__convo-card-content-wrapper fl">
          <div class="msg-conversation-card__row align-items-center display-flex">
            <h3 class="msg-conversation-listitem__participant-names msg-conversation-card__participant-names truncate t-14 t-black
                t-normal">
              Mark Stevenson
            </h3>
            <div class="msg-conversation-card__mute-icon-holder
                msg-conversation-card__mute-icon-holder--inbox-shortcuts">
<!---->            </div>
              <time class="msg-overlay-list-bubble-item__time-stamp t-12
                  msg-overlay-list-bubble-item__time-stamp--inbox-shortcuts
                  t-normal t-black--light">
                Apr 9
              </time>
              <div class="msg-overlay-list-bubble__inbox-shortcuts-container">
                <div class="msg-overlay-list-bubble__inbox-shortcuts">
                  

<div id="ember211" class="artdeco-dropdown msg-thread-actions__dropdown artdeco-dropdown--placement-bottom artdeco-dropdown--justification-right ember-view">
  <button aria-expanded="false" id="ember212" class="msg-thread-actions__control artdeco-button artdeco-button--circle artdeco-button--1 artdeco-button--muted artdeco-button--tertiary artdeco-dropdown__trigger artdeco-dropdown__trigger--placement-bottom ember-view" type="button" tabindex="0">
    <li-icon aria-hidden="true" type="ellipsis-horizontal-icon" class="artdeco-button__icon" size="small" color="true"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" data-supported-dps="16x16" fill="currentColor" class="mercado-match" width="16" height="16" focusable="false">
  <path d="M3 9.5A1.5 1.5 0 114.5 8 1.5 1.5 0 013 9.5zM11.5 8A1.5 1.5 0 1013 6.5 1.5 1.5 0 0011.5 8zm-5 0A1.5 1.5 0 108 6.5 1.5 1.5 0 006.5 8z"></path>
</svg></li-icon>
    <span class="visually-hidden">
      Open the options list in your conversation with Mark Stevenson and Harith Al-Safi
    </span>
  
<!----></button>
  <div class="msg-thread-actions__dropdown-container">
    <div tabindex="-1" aria-hidden="true" id="ember213" class="msg-thread-actions__dropdown-options--inbox-shortcuts artdeco-dropdown__content artdeco-dropdown--is-dropdown-element artdeco-dropdown__content--has-arrow artdeco-dropdown__content--arrow-right artdeco-dropdown__content--justification-right artdeco-dropdown__content--placement-bottom ember-view"><!----></div>
  </div>
</div>

<!---->

<div>
<!----></div>

<!---->
                </div>
              </div>
          </div>

          <div class="msg-conversation-card__row justify-space-between">
            <div class="msg-overlay-list-bubble__message-snippet-container--narrow-two-line">
<!---->              <p class="msg-overlay-list-bubble__message-snippet--v2
                  
                  m0 t-12
                  t-black--light">
<!----><!---->                You: Dear Mark 
I hope you are doing well
I saw that you work in Splunk Talent team, and I saw that there is a pending software engineering summer internship in London. Just wanted to see if its still available and if there are any tips for getting that role.
Thank you!
              </p>
<!---->            </div>
            <div class="display-flex">
              <div class="msg-conversation-card__conversation-status msg-conversation-card__star-icon
                  ">
<!---->              </div>
<!---->            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
        <div class="msg-conversation-listitem__link msg-overlay-list-bubble__convo-item" tabindex="0" role="button" id="overlay-conversation-card-ember214" data-feedback-redacted="">
  <div class="msg-overlay-list-bubble__convo-card-container">
    <div class="msg-conversation-card msg-overlay-list-bubble__convo-card display-flex">
      <div class="msg-selectable-entity
    
    msg-selectable-entity--3">
      <div class="msg-facepile-grid--no-facepile msg-facepile-grid
    msg-facepile-grid--3 msg-selectable-entity__entity">
<!---->      <img src="https://media.licdn.com/dms/image/C4E03AQE6fQ2HPbgb6A/profile-displayphoto-shrink_100_100/0/1517561481934?e=1691625600&amp;v=beta&amp;t=vw1zWgT6XPM2UYme66Od2iz9-G07Wbld2yZI5ngr654" loading="lazy" alt="Chris Griffin" id="ember239" class="evi-image lazy-image msg-facepile-grid__img msg-facepile-grid__img--person ember-view">
</div>
      <div class="msg-selectable-entity__checkbox-container">
    <input id="checkbox-msg-selectable-entity__checkbox-ember215" class="ember-checkbox ember-view msg-selectable-entity__input simple-form" type="checkbox">
    <label class="msg-selectable-entity__checkbox-label ml2" aria-label="Select conversation" for="checkbox-msg-selectable-entity__checkbox-ember215">
    </label>

    <div class="msg-selectable-entity__checkbox-circle-container">
      <div class="msg-selectable-entity__checkbox-circle">
      </div>
    </div>
  </div>
</div>

      <div class="overflow-hidden pl2
          msg-overlay-list-bubble__convo-card-content">
        <div class="msg-overlay-list-bubble__convo-card-content-wrapper fl">
          <div class="msg-conversation-card__row align-items-center display-flex">
            <h3 class="msg-conversation-listitem__participant-names msg-conversation-card__participant-names truncate t-14 t-black
                t-normal">
              Chris Griffin
            </h3>
            <div class="msg-conversation-card__mute-icon-holder
                msg-conversation-card__mute-icon-holder--inbox-shortcuts">
<!---->            </div>
              <time class="msg-overlay-list-bubble-item__time-stamp t-12
                  msg-overlay-list-bubble-item__time-stamp--inbox-shortcuts
                  t-normal t-black--light">
                Apr 3
              </time>
              <div class="msg-overlay-list-bubble__inbox-shortcuts-container">
                <div class="msg-overlay-list-bubble__inbox-shortcuts">
                  

<div id="ember217" class="artdeco-dropdown msg-thread-actions__dropdown artdeco-dropdown--placement-bottom artdeco-dropdown--justification-right ember-view">
  <button aria-expanded="false" id="ember218" class="msg-thread-actions__control artdeco-button artdeco-button--circle artdeco-button--1 artdeco-button--muted artdeco-button--tertiary artdeco-dropdown__trigger artdeco-dropdown__trigger--placement-bottom ember-view" type="button" tabindex="0">
    <li-icon aria-hidden="true" type="ellipsis-horizontal-icon" class="artdeco-button__icon" size="small" color="true"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" data-supported-dps="16x16" fill="currentColor" class="mercado-match" width="16" height="16" focusable="false">
  <path d="M3 9.5A1.5 1.5 0 114.5 8 1.5 1.5 0 013 9.5zM11.5 8A1.5 1.5 0 1013 6.5 1.5 1.5 0 0011.5 8zm-5 0A1.5 1.5 0 108 6.5 1.5 1.5 0 006.5 8z"></path>
</svg></li-icon>
    <span class="visually-hidden">
      Open the options list in your conversation with Chris Griffin and Harith Al-Safi
    </span>
  
<!----></button>
  <div class="msg-thread-actions__dropdown-container">
    <div tabindex="-1" aria-hidden="true" id="ember219" class="msg-thread-actions__dropdown-options--inbox-shortcuts artdeco-dropdown__content artdeco-dropdown--is-dropdown-element artdeco-dropdown__content--has-arrow artdeco-dropdown__content--arrow-right artdeco-dropdown__content--justification-right artdeco-dropdown__content--placement-bottom ember-view"><!----></div>
  </div>
</div>

<!---->

<div>
<!----></div>

<!---->
                </div>
              </div>
          </div>

          <div class="msg-conversation-card__row justify-space-between">
            <div class="msg-overlay-list-bubble__message-snippet-container--narrow-two-line">
<!---->              <p class="msg-overlay-list-bubble__message-snippet--v2
                  
                  m0 t-12
                  t-black--light">
<!----><!---->                Software engineer vacancies!
              </p>
<!---->            </div>
            <div class="display-flex">
              <div class="msg-conversation-card__conversation-status msg-conversation-card__star-icon
                  ">
<!---->              </div>
<!---->            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
</div>

<!---->
<!----><!---->
              <div data-test-msg-cross-pillar-visible-beacon="">
  
</div>
<!---->          </div>
        </section>

<!----><!----></div>

<!---->
<!---->
  <div id="msg-overlay__emoji-hoverable-outlet"></div>

  <div id="msg-overlay__reactor-list-outlet"></div>
</aside>

<!---->
    
      <div id="ember28" class="ember-view"><!----></div>
  


    <img src="https://px.ads.linkedin.com/collect/?pid=6883&amp;fmt=gif&amp;_t=1686261664768" alt="" role="none" class="third-party-tracking-pixel hidden" data-test-third-party-tracking-pixel="" klr8snozv="">


</div>

<div id="artdeco-hoverable-outlet"></div>

<!---->
<div id="type-ahead-wormhole" class="type-ahead type-ahead-wormhole">
</div>

<div id="toast-wormhole" class="toast-wormhole">
</div>

<div id="profile-inline-modal-outlet">
</div>

<!---->
<div><!----></div>
<code style="display: none" id="datalet-bpr-guid-104273">
  {"request":"/voyager/api/identity/dash/profiles?q\u003DmemberIdentity\u0026memberIdentity\u003Dharith-al-safi\u0026decorationId\u003Dcom.linkedin.voyager.dash.deco.identity.profile.WebTopCardCore-19","status":200,"body":"bpr-guid-104273","method":"GET","headers":{"x-li-uuid":"AAX9pWM/tcB+TnflXcw30Q\u003D\u003D"}}
</code>
<img src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" style="display: none" class="datalet-bpr-guid-104273"><script type="x/boundary" id="fastboot-body-start"></script><script type="x/boundary" id="fastboot-body-end"></script><code style="display: none" id="clientPageInstance">
  urn:li:page:d_flagship3_profile_view_base_education_details;8786852b-22d5-429d-90c2-b17f92117f52
</code>

<img src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" style="display: none" class="terminatorlet">



    <div id="a11y-notification" class="visually-hidden" role="region" aria-live="polite"></div>
  

</body>
'''

# Parse the HTML content
soup = BeautifulSoup(html, 'html.parser')

# Find all education items
education_items = soup.find_all('li', class_='pvs-list__paged-list-item')

# Create a list to store the extracted information
education_list = []

# Extract information from each education item
for item in education_items:
    education_info = {}
    
    # Extract university name and degree
    university_element = item.find('div', class_='display-flex flex-wrap align-items-center full-height').find('span')
    if university_element:        
      university_name = university_element.get_text(strip=True)
    else:
      university_name = "N/A"  # or any default value you prefer

    degree = item.find('span', class_='t-14').get_text(strip=True)
    
    # Extract date range
    date_range_element = item.find('span', class_='t-14 t-normal t-black--light')
    if date_range_element:
      date_range = date_range_element.find('span').get_text(strip=True)
    else:
      date_range = "N/A"  # or any default value you prefer
    
    # Extract additional details
    additional_details = item.find('div', class_='pvs-list__outer-container').get_text(strip=True)
    
    # Store the extracted information in the dictionary
    education_info['university_name'] = university_name
    education_info['degree'] = degree
    education_info['date_range'] = date_range
    education_info['additional_details'] = additional_details
    
    # Append the dictionary to the list
    education_list.append(education_info)

# Write the extracted information to a JSON file
with open('education.json', 'w') as file:
    json.dump(education_list, file, indent=4)
