BEGIN;
--
-- Create model Movie
--
CREATE TABLE "movie_movie" ("movie_id" integer NOT NULL PRIMARY KEY, "movie_title" varchar(200) NOT NULL, "movie_slug" varchar(200) NOT NULL, "movie_release" timestamp with time zone NULL, "movie_imdb" double precision NULL, "movie_rt" integer NULL, "movie_rating" varchar(3) NOT NULL, "movie_popularity" double precision NULL, "movie_desc" text NULL, "movie_runtime" integer NULL, "movie_yt" varchar(100) NULL);
--
-- Create model People
--
CREATE TABLE "movie_people" ("people_id" integer NOT NULL PRIMARY KEY, "people_name" varchar(200) NOT NULL, "people_slug" varchar(220) NOT NULL, "people_gender" varchar(2) NOT NULL, "people_desc" text NULL, "people_profession" varchar(20) NOT NULL, "people_dob" date NULL, "people_img" varchar(400) NULL);
--
-- Create model Studio
--
CREATE TABLE "movie_studio" ("studio_id" varchar(4) NOT NULL PRIMARY KEY, "studio_name" varchar(100) NOT NULL, "studio_slug" varchar(120) NOT NULL, 
"studio_area" varchar(30) NOT NULL, "studio_hq" varchar(120) NOT NULL);
--
-- Create model ReleaseData
--
CREATE TABLE "movie_releasedata" ("id" bigserial NOT NULL PRIMARY KEY, "release_id" varchar(10) NOT NULL, "country" varchar(50) NOT NULL, "release_date" date NOT NULL, "movie_id_id" integer NOT NULL);
--
-- Create model MovieGenre
--
CREATE TABLE "movie_moviegenre" ("id" bigserial NOT NULL PRIMARY KEY, "mg_genre" varchar(20) NOT NULL, "mg_movie_id" integer NOT NULL);
--
-- Create model MovieCredit
--
CREATE TABLE "movie_moviecredit" ("id" bigserial NOT NULL PRIMARY KEY, "mc_role" varchar(60) NOT NULL, "mc_movie_id" integer NOT NULL, "mc_people_id" integer NOT NULL);
--
-- Create model MovieCast
--
CREATE TABLE "movie_moviecast" ("id" bigserial NOT NULL PRIMARY KEY, "mc_char" varchar(40) NOT NULL, "mc_movie_id" integer NOT NULL, "mc_star_id" integer NOT NULL);
--
-- Add field movie_director to movie
--
ALTER TABLE "movie_movie" ADD COLUMN "movie_director_id" integer NOT NULL CONSTRAINT "movie_movie_movie_director_id_1634415a_fk_movie_peo" REFERENCES "movie_people"("people_id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "movie_movie_movie_director_id_1634415a_fk_movie_peo" IMMEDIATE;       
--
-- Add field movie_studio to movie
--
ALTER TABLE "movie_movie" ADD COLUMN "movie_studio_id" varchar(4) NOT NULL CONSTRAINT "movie_movie_movie_studio_id_294c2a92_fk_movie_studio_studio_id" REFERENCES "movie_studio"("studio_id") DEFERRABLE INITIALLY DEFERRED; SET CONSTRAINTS "movie_movie_movie_studio_id_294c2a92_fk_movie_studio_studio_id" IMMEDIATE;
--
-- Create model Certificate
--
CREATE TABLE "movie_certificate" ("id" bigserial NOT NULL PRIMARY KEY, "certificate_id" varchar(30) NOT NULL, "movie_rating" varchar(3) NOT NULL, "issue_authority" varchar(50) NOT NULL, "movie_id_id" integer NOT NULL);
CREATE INDEX "movie_studio_studio_id_8d3b4e0c_like" ON "movie_studio" ("studio_id" varchar_pattern_ops);
ALTER TABLE "movie_releasedata" ADD CONSTRAINT "movie_releasedata_movie_id_id_e827e94e_fk_movie_movie_movie_id" FOREIGN KEY ("movie_id_id") REFERENCES "movie_movie" ("movie_id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "movie_releasedata_movie_id_id_e827e94e" ON "movie_releasedata" ("movie_id_id");
ALTER TABLE "movie_moviegenre" ADD CONSTRAINT "movie_moviegenre_mg_movie_id_94dd2e9c_fk_movie_movie_movie_id" FOREIGN KEY ("mg_movie_id") REFERENCES "movie_movie" ("movie_id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "movie_moviegenre_mg_movie_id_94dd2e9c" ON "movie_moviegenre" ("mg_movie_id");
ALTER TABLE "movie_moviecredit" ADD CONSTRAINT "movie_moviecredit_mc_movie_id_8d80fc08_fk_movie_movie_movie_id" FOREIGN KEY ("mc_movie_id") REFERENCES "movie_movie" ("movie_id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "movie_moviecredit" ADD CONSTRAINT "movie_moviecredit_mc_people_id_208a017d_fk_movie_peo" FOREIGN KEY ("mc_people_id") REFERENCES "movie_people" ("people_id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "movie_moviecredit_mc_movie_id_8d80fc08" ON "movie_moviecredit" ("mc_movie_id");
CREATE INDEX "movie_moviecredit_mc_people_id_208a017d" ON "movie_moviecredit" ("mc_people_id");
ALTER TABLE "movie_moviecast" ADD CONSTRAINT "movie_moviecast_mc_movie_id_4cc58b61_fk_movie_movie_movie_id" FOREIGN KEY ("mc_movie_id") REFERENCES "movie_movie" ("movie_id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "movie_moviecast" ADD CONSTRAINT "movie_moviecast_mc_star_id_1851e000_fk_movie_people_people_id" FOREIGN KEY ("mc_star_id") REFERENCES "movie_people" ("people_id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "movie_moviecast_mc_movie_id_4cc58b61" ON "movie_moviecast" ("mc_movie_id");
CREATE INDEX "movie_moviecast_mc_star_id_1851e000" ON "movie_moviecast" ("mc_star_id");
CREATE INDEX "movie_movie_movie_director_id_1634415a" ON "movie_movie" ("movie_director_id");
CREATE INDEX "movie_movie_movie_studio_id_294c2a92" ON "movie_movie" ("movie_studio_id");
CREATE INDEX "movie_movie_movie_studio_id_294c2a92_like" ON "movie_movie" ("movie_studio_id" varchar_pattern_ops);
ALTER TABLE "movie_certificate" ADD CONSTRAINT "movie_certificate_movie_id_id_06452016_fk_movie_movie_movie_id" FOREIGN KEY ("movie_id_id") REFERENCES "movie_movie" ("movie_id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "movie_certificate_movie_id_id_06452016" ON "movie_certificate" ("movie_id_id");
COMMIT;