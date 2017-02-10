# -*- coding: utf-8 -*-

from gluon import current
from s3 import *
from s3layouts import *
try:
    from .layouts import *
except ImportError:
    pass
import s3menus as default

# =============================================================================
class S3OptionsMenu(default.S3OptionsMenu):
    """ Custom Controller Menus """

    # -------------------------------------------------------------------------
    def vol(self):
        """ Volunteer Management """

        s3 = current.session.s3
        ADMIN = s3.system_roles.ADMIN

        # Custom conditions for the check-hook, as lambdas in order
        # to have them checked only immediately before rendering:
        is_org_admin = lambda i: s3.hrm.orgs and True or \
                                 ADMIN in s3.roles

        settings = current.deployment_settings
        #show_programmes = lambda i: settings.get_hrm_vol_experience() == "programme"
        #show_tasks = lambda i: settings.has_module("project") and \
        #                       settings.get_project_mode_task()
        teams = settings.get_hrm_teams()
        use_teams = lambda i: teams

        #check_org_dependent_field = lambda tablename, fieldname: \
        #    settings.set_org_dependent_field(tablename, fieldname,
        #                                     enable_field = False)

        return M(c="vol")(
                    M("Volunteers", f="volunteer")(
                        M("Create Volunteer", m="create"),
                        #M("List All"),
                        M("Import", f="person", m="import",
                          vars={"group":"volunteer"}, p="create"),
                    ),
                    M(teams, f="group", check=use_teams)(
                        M("Create Team", m="create"),
                        #M("List All"),
                        M("Search Members", f="group_membership"),
                    ),
                    #M("Department Catalog", f="department")(
                    #    M("New", m="create"),
                    #    M("List All"),
                    #),
                    #M("Volunteer Role Catalog", f="job_title")(
                    #    M("New", m="create"),
                    #    M("List All"),
                    #    M("Import", m="import", p="create", check=is_org_admin),
                    #),
                    #M("Skill Catalog", f="skill")(
                    #    M("New", m="create"),
                    #    M("List All"),
                    #    #M("Skill Provisions", f="skill_provision"),
                    #),
                    M("Training Events", f="training_event")(
                        M("Create Event", m="create"),
                        #M("List All"),
                        M("Search Training Participants", f="training"),
                        M("Import Participant List", f="training", m="import"),
                    ),
                    M("Training Course Catalog", f="course")(
                        M("Create Course", m="create"),
                        #M("List All"),
                        #M("Course Certificates", f="course_certificate"),
                    ),
                    M("Certificate Catalog", f="certificate")(
                        M("Create Certificate", m="create"),
                        #M("List All"),
                        #M("Skill Equivalence", f="certificate_skill"),
                    ),
                    #M("Programs", f="programme", check=show_programmes)(
                    #    M("New", m="create"),
                    #    #M("List All"),
                    #    M("Import Hours", f="programme_hours", m="import"),
                    #),
                    M("Reports", f="volunteer", m="report")(
                        M("Volunteer Report", m="report"),
                        M("Training Report", f="training", m="report"),
                    ),
                )

# END =========================================================================

