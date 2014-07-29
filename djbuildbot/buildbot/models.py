from __future__ import unicode_literals

from django.db import models

class BuildrequestClaims(models.Model):
    brid = models.IntegerField(unique=True, null=True, blank=True)
    objectid = models.IntegerField(null=True, blank=True)
    claimed_at = models.IntegerField()
    class Meta:
        db_table = 'buildrequest_claims'

class Buildrequests(models.Model):
    id = models.IntegerField(primary_key=True)
    buildsetid = models.IntegerField()
    buildername = models.CharField(max_length=256)
    priority = models.IntegerField()
    complete = models.IntegerField(null=True, blank=True)
    results = models.SmallIntegerField(null=True, blank=True)
    submitted_at = models.IntegerField()
    complete_at = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'buildrequests'

class Builds(models.Model):
    id = models.IntegerField(primary_key=True)
    number = models.IntegerField()
    brid = models.IntegerField()
    start_time = models.IntegerField()
    finish_time = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'builds'

class BuildsetProperties(models.Model):
    buildsetid = models.IntegerField()
    property_name = models.CharField(max_length=256)
    property_value = models.CharField(max_length=1024)
    class Meta:
        db_table = 'buildset_properties'

class Buildsets(models.Model):
    id = models.IntegerField(primary_key=True)
    external_idstring = models.CharField(max_length=256, blank=True)
    reason = models.CharField(max_length=256, blank=True)
    sourcestampsetid = models.IntegerField()
    submitted_at = models.IntegerField()
    complete = models.SmallIntegerField()
    complete_at = models.IntegerField(null=True, blank=True)
    results = models.SmallIntegerField(null=True, blank=True)
    class Meta:
        db_table = 'buildsets'

class ChangeFiles(models.Model):
    changeid = models.IntegerField()
    filename = models.CharField(max_length=1024)
    class Meta:
        db_table = 'change_files'

class ChangeProperties(models.Model):
    changeid = models.IntegerField()
    property_name = models.CharField(max_length=256)
    property_value = models.CharField(max_length=1024)
    class Meta:
        db_table = 'change_properties'

class ChangeUsers(models.Model):
    changeid = models.IntegerField()
    uid = models.IntegerField()
    class Meta:
        db_table = 'change_users'

class Changes(models.Model):
    changeid = models.IntegerField(primary_key=True)
    author = models.CharField(max_length=256)
    comments = models.CharField(max_length=1024)
    is_dir = models.SmallIntegerField()
    branch = models.CharField(max_length=256, blank=True)
    revision = models.CharField(max_length=256, blank=True)
    revlink = models.CharField(max_length=256, blank=True)
    when_timestamp = models.IntegerField()
    category = models.CharField(max_length=256, blank=True)
    repository = models.CharField(max_length=512)
    project = models.CharField(max_length=512)
    codebase = models.CharField(max_length=256)
    class Meta:
        db_table = 'changes'

class MigrateVersion(models.Model):
    repository_id = models.CharField(max_length=250, unique=True)
    repository_path = models.TextField(blank=True)
    version = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'migrate_version'

class ObjectState(models.Model):
    objectid = models.IntegerField()
    name = models.CharField(max_length=256)
    value_json = models.TextField()
    class Meta:
        db_table = 'object_state'

class Objects(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=128)
    class_name = models.CharField(max_length=128)
    class Meta:
        db_table = 'objects'

class Patches(models.Model):
    id = models.IntegerField(primary_key=True)
    patchlevel = models.IntegerField()
    patch_base64 = models.TextField()
    subdir = models.TextField(blank=True)
    patch_author = models.TextField()
    patch_comment = models.TextField()
    class Meta:
        db_table = 'patches'

class SchedulerChanges(models.Model):
    objectid = models.IntegerField(null=True, blank=True)
    changeid = models.IntegerField(null=True, blank=True)
    important = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'scheduler_changes'

class SourcestampChanges(models.Model):
    sourcestampid = models.IntegerField()
    changeid = models.IntegerField()
    class Meta:
        db_table = 'sourcestamp_changes'

class Sourcestamps(models.Model):
    id = models.IntegerField(primary_key=True)
    branch = models.CharField(max_length=256, blank=True)
    revision = models.CharField(max_length=256, blank=True)
    patchid = models.IntegerField(null=True, blank=True)
    repository = models.TextField()
    project = models.TextField()
    sourcestampsetid = models.IntegerField()
    codebase = models.CharField(max_length=256)
    class Meta:
        db_table = 'sourcestamps'

class Sourcestampsets(models.Model):
    id = models.IntegerField(primary_key=True)
    class Meta:
        db_table = 'sourcestampsets'

class Users(models.Model):
    uid = models.IntegerField(primary_key=True)
    identifier = models.CharField(max_length=256, unique=True)
    bb_username = models.CharField(max_length=128, unique=True, blank=True)
    bb_password = models.CharField(max_length=128, blank=True)
    class Meta:
        db_table = 'users'

class UsersInfo(models.Model):
    uid = models.IntegerField()
    attr_type = models.CharField(max_length=128)
    attr_data = models.CharField(max_length=128)
    class Meta:
        db_table = 'users_info'

